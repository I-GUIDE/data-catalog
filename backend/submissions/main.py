import asyncio
import logging
import uvicorn

from api import app as app_fastapi

class Server(uvicorn.Server):
    def handle_exit(self, sig: int, frame) -> None:
        #app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    server = Server(config=uvicorn.Config(app_fastapi, workers=1, loop="asyncio", host="0.0.0.0", port=5002))
    #settings = get_settings()
    api = asyncio.create_task(server.serve())
    await asyncio.wait([api])


if __name__ == "__main__":
    # Run all applications
    asyncio.run(main())
