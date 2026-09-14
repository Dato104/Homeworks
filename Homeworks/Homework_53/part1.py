from dotenv import load_dotenv
from google import genai
import os
from google.genai.errors import ClientError



load_dotenv(".env")


MODEL = "gemini-3.6-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


text_short = "Fast, reliable, and designed to perform when it matters most."
text_medium = "Built for clarity and efficiency, this solution helps you streamline your workflow, stay organized, and handle daily tasks effortlessly without unneeded complexity."
text_long = """ When long-term growth and operational excellence depend on modernizing everyday practices, having a reliable framework in place makes all the difference. Technology continuously shapes how teams organize projects, solve unexpected challenges, and scale their reach, but success ultimate relies on having systems that remain clear, responsive, and adaptable.
                By eliminating needless friction and prioritizing intuitive structure, modern platforms allow organizations to stay fully aligned on their core goals. Rather than spending valuable time managing disconnected tools or navigating overly complex processes, teams can focus their energy directly on innovation, strategy, and execution. Structured digital workflows provide complete visibility across tasks, ensuring that every contributor understands their role, monitors progress effectively, and addresses potential roadblocks well before they escalate into major obstacles.
                Furthermore, long-term stability requires solutions that accommodate evolution over time. As project demands expand and priorities shift, rigid structures quickly become major bottlenecks. Adaptable architecture ensures that as workload volume increases, systems scale smoothly without sacrificing performance, security, or output quality.
                Ultimately, true productivity is not about working longer hours or using more software; it is about establishing smart, standardized habits supported by reliable tools. By focusing on essential functionality, practical organization, and consistent execution, teams can maintain steady momentum, hit ambitious deadlines, and build a solid foundation for sustainable future success."
                By eliminating needless friction and prioritizing intuitive structure, modern platforms allow organizations to stay fully aligned on their core goals. Rather than spending valuable time managing disconnected tools or navigating overly complex processes, teams can focus their energy directly on innovation, strategy, and execution. Structured digital workflows provide complete visibility across tasks, ensuring that every contributor understands their role, monitors progress effectively, and addresses potential roadblocks well before they escalate into major obstacles.
"""


def count_text_tokens(text):

    token_count = client.models.count_tokens(
        model=MODEL,
        contents=text
    )

    if token_count.total_tokens == 0:
        print("No text tokens found")

    if token_count.total_tokens > 300:
        raise ClientError(response_json={"message": f"Too much token count: {token_count.total_tokens}"}, code=429)

    else:
        print(f"Token count is valid: {token_count.total_tokens}")


count_text_tokens(text_short)
count_text_tokens(text_medium)
count_text_tokens(text_long)












