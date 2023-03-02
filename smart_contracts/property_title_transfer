import xrpl
from xrpl.models.transactions import EscrowCreate
from xrpl.wallet import Wallet

# Connect to the XRPL Testnet
client = xrpl.clients.JsonRpcClient('https://s.altnet.rippletest.net:51234')

# Set up the wallet for the property owner
wallet = Wallet(seed='shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

# Create the EscrowCreate transaction to create a new token
escrow_create = EscrowCreate(
    account=wallet.classic_address,
    amount='100000000', # Token amount
    destination='rrrrrrrrrrrrrrrrrrrrr', # Destination address
    cancel_after=1000000, # Block number after which escrow can be cancelled
    finish_after=500000, # Block number after which escrow can be executed
    condition='ff' # Condition for executing escrow
)

# Sign and submit the transaction to the XRPL
response = client.submit(escrow_create, wallet)
