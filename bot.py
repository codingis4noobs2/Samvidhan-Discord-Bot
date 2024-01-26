import pandas as pd
import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='%', intents=intents)

indian_constitution_parts_df = pd.read_csv('data/Indian_Constitution_Parts.csv')

def parse_articles_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        articles_text = file.read()
        
    articles = []
    for line in articles_text.strip().split('\n'):
        parts = line.split(' – ', 1)
        if len(parts) == 2:
            article_number = parts[0].strip()
            summary = parts[1].strip()
            articles.append((article_number, summary))
    return articles

# Use the function to parse articles
parsed_articles = parse_articles_from_file('data/articles.txt')

def create_articles_embed(articles, start_index):
    embed = nextcord.Embed(title="Articles Summary", description="Summaries of the Indian Constitution Articles", color=0x1F8B4C)
    for i in range(start_index, min(start_index + 10, len(articles))):  # Changed from 5 to 10
        article_number, summary = articles[i]
        embed.add_field(name=article_number, value=summary, inline=False)
    return embed

# View for pagination
class PaginationView(View):
    def __init__(self, articles):
        super().__init__()
        self.articles = articles
        self.current_page = 0
        self.articles_per_page = 10

    @nextcord.ui.button(label="Backward", style=nextcord.ButtonStyle.red)
    async def backward_button_callback(self, button, interaction):
        if self.current_page > 0:
            self.current_page -= 1
            embed = create_articles_embed(self.articles, self.current_page * self.articles_per_page)
            await interaction.message.edit(embed=embed, view=self)

    @nextcord.ui.button(label="Forward", style=nextcord.ButtonStyle.green)
    async def forward_button_callback(self, button, interaction):
        if (self.current_page + 1) * self.articles_per_page < len(self.articles):
            self.current_page += 1
            embed = create_articles_embed(self.articles, self.current_page * self.articles_per_page)
            await interaction.message.edit(embed=embed, view=self)


@bot.slash_command(description="Displays a summary of all articles with pagination")
async def all_articles(interaction: nextcord.Interaction):
    embed = create_articles_embed(parsed_articles, 0)
    view = PaginationView(parsed_articles)
    await interaction.send(embed=embed, view=view)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print(f'Bot ID: {bot.user.id}')
    await bot.change_presence(activity=nextcord.Game(name="Type `/help` for commands"))

@bot.slash_command(description="Displays all the available commands and their descriptions")
async def help(interaction: nextcord.Interaction):
    embed = nextcord.Embed(
        title="Samvidhan Bot Help",
        description="Here are the commands you can use:",
        color=0x1F8B4C
    )
    
    embed.add_field(
        name="/help",
        value="Displays all commands with their descriptions.",
        inline=False
    )
    embed.add_field(
        name="/about",
        value="Displays information about the bot.",
        inline=False
    )
    embed.add_field(
        name="/all_articles",
        value="Displays all articles with a summary table and pagination.",
        inline=False
    )
    embed.add_field(
        name="/part_details",
        value="Provides details and summary of different parts of the Indian Constitution with pagination.",
        inline=False
    )
    embed.add_field(
        name="/search_article <article_number>",
        value="Searches for an article by its number and displays the information.",
        inline=False
    )
    # Add more fields for additional commands as needed

    await interaction.response.send_message(embed=embed)

class PartsPaginationView(nextcord.ui.View):
    def __init__(self, parts, embeds_per_page=5):
        super().__init__()
        self.parts = parts
        self.embeds_per_page = embeds_per_page
        self.current_page = 0
        self.max_page = (len(self.parts) - 1) // embeds_per_page
        self.update_buttons()

    @nextcord.ui.button(label="Backward", style=nextcord.ButtonStyle.red)
    async def backward_button_callback(self, button, interaction):
        if self.current_page > 0:
            self.current_page -= 1
            embeds = create_parts_embeds(self.parts, self.current_page, self.embeds_per_page)
            await interaction.response.edit_message(embeds=embeds, view=self)
            self.update_buttons()

    @nextcord.ui.button(label="Forward", style=nextcord.ButtonStyle.green)
    async def forward_button_callback(self, button, interaction):
        if self.current_page < self.max_page:
            self.current_page += 1
            embeds = create_parts_embeds(self.parts, self.current_page, self.embeds_per_page)
            await interaction.response.edit_message(embeds=embeds, view=self)
            self.update_buttons()

    def update_buttons(self):
        self.children[0].disabled = self.current_page == 0
        self.children[1].disabled = self.current_page == self.max_page

def create_parts_embeds(parts_df, page, embeds_per_page):
    start = page * embeds_per_page
    end = start + embeds_per_page
    embeds = []
    for _, row in parts_df.iloc[start:end].iterrows():
        embed = nextcord.Embed(
            title=row['Subject Mentioned in the Part'],
            description=f"Articles Included: {row['Articles in Indian Constitution']}",
            color=0x1F8B4C
        )
        embeds.append(embed)
    return embeds

@bot.slash_command(description="Provides details and summary of different parts of the Indian Constitution")
async def part_details(interaction: nextcord.Interaction):
    # Get the initial set of embeds to display
    initial_embeds = create_parts_embeds(indian_constitution_parts_df, 0, 5)
    # Create the view for pagination
    view = PartsPaginationView(indian_constitution_parts_df, embeds_per_page=5)
    # Send the message with the initial embeds and the view for pagination
    await interaction.response.send_message(embeds=initial_embeds, view=view)

@bot.slash_command(description="Displays information about the bot")
async def about(interaction: nextcord.Interaction):
    embed = nextcord.Embed(
        title="About Samvidhan Bot",
        description="Dedicated to making the Indian Constitution more accessible.",
        color=0x1F8B4C
    )
    embed.add_field(name="What can I do?", value="I can fetch articles, search by description, provide summaries, and more.", inline=False)
    embed.add_field(name="Language Support", value="I provide information in both English and Hindi to cater to a diverse user base.", inline=False)
    embed.add_field(name="Get Started", value="Use /help to see all the commands available.", inline=False)
    embed.set_footer(text="Here to help you explore the Indian Constitution")

    await interaction.send(embed=embed)

@bot.slash_command(description="Fetches information about a specific article from the Indian Constitution")
async def search_article(interaction: nextcord.Interaction, article_query: str):
    # Trim spaces and make the search case-insensitive
    article_query = article_query.strip().lower()
    
    # Find the requested article
    article_info = None
    for article_num, summary in parsed_articles:
        # Remove 'Article' prefix and any spaces for comparison
        if article_num.lower().replace('article', '').strip() == article_query:
            article_info = f"{article_num}: {summary}"
            break

    # Respond with the article information or a not found message
    if article_info:
        await interaction.response.send_message(article_info)
    else:
        await interaction.response.send_message(f"Article {article_query.upper()} not found.")

bot.run('token')
