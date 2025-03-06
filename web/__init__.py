from aiohttp import web
from web.stream_routes import routes

# Health check endpoint for Koyeb
async def health_check(request):
    return web.Response(text="Bot is alive!", status=200)

# Create the web app
web_app = web.Application()
web_app.add_routes(routes)  # Your existing routes from stream_routes
web_app.add_routes([web.get('/', health_check)])  # Add health check route