import xrpl
from xrpl.models.transactions import EscrowFinish, EscrowCreate
from xrpl.wallet import Wallet

# Connect to the XRPL Testnet
client = xrpl.clients.JsonRpcClient('https://s.altnet.rippletest.net:51234')

# Set up the wallet for the buyer
buyer_wallet = Wallet(seed='shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

# Set up the wallet for the seller
seller_wallet = Wallet(seed='ssssssssssssssssssssssssssssssss')

# Create the EscrowCreate transaction to hold funds in escrow
escrow_create = EscrowCreate(
    account=seller_wallet.classic_address,
    amount='100000000', # Amount to hold in escrow
    destination=buyer_wallet.classic_address, # Destination address
    cancel_after=1000000, # Block number after which escrow can be cancelled
    finish_after=500000, # Block number after which escrow can be executed
    condition='ff' # Condition for executing escrow
)

# Sign and submit the transaction to the XRPL
response = client.submit(escrow_create, seller_wallet)

# Get the escrow ID from the response
escrow_id = response.result['tx_json']['EscrowCreate']['escrow']

# Create the EscrowFinish transaction to release funds from escrow
escrow_finish = EscrowFinish(
    account=seller_wallet.classic_address,
    owner=buyer_wallet.classic_address, # Owner of escrowed funds
    escrow_sequence=escrow_id, # Escrow ID
    condition='ff' # Condition for releasing escrowed funds
)

# Sign and submit the transaction to the XRPL
response = client.submit(escrow_finish, buyer_wallet)
