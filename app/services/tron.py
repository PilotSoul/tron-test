from tronpy import AsyncTron


async def get_wallet_resources(address):
    async with AsyncTron(network="shasta") as client:
        bandwidth = await client.get_bandwidth(address)

        energy_info = await client.get_account_resource(address)
        energy = energy_info.get("EnergyLimit", 0) - energy_info.get("EnergyUsed", 0)

        account = await client.get_account(address)
        balance = account["balance"]

        return {"bandwidth": bandwidth, "energy": energy, "balance": balance}
