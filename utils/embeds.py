import discord

def user_embed(data):
    embed = discord.Embed(
        title=f"User Info - {data['name']}",
        color=discord.Color.blurple()
    )

    embed.add_field(name="Display Name", value=data["display_name"])
    embed.add_field(name="User ID", value=data["id"])
    embed.add_field(name="Created At", value=data["created_at"].strftime("%Y-%m-%d"))

    embed.set_thumbnail(url=data["avatar"])

    return embed

def avatar_embed(data):
    embed=discord.Embed(
        title=f"{data['name']}'s Avatar",
        color=discord.Color.blurple()
    )
    
    embed.set_image(url=data["avatar"])     
    return embed
