import asyncio
import chromadb

async def main():
    client = await chromadb.AsyncHttpClient()
    collection = await client.create_collection(name="async_collection")

    await collection.add(
        documents=["hello async client"],
        ids=["id1"]
    )

asyncio.run(main())