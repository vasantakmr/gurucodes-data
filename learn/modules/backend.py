import os 
import json
data ={
  "backend-development-overview": {
    "title": "Backend Development Overview",
    "description": "Detailed Overview of Backend Development",
    "slug": "backend-development-overview",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
      {
        "name": "What is Backend Development?",
        "slug": "what-is-backend-development",
      },
      {
        "name": "Skills and Concepts",
        "slug": "skills-concepts",
      }
    ],
  },
  "programming-languages":{
      "title": "Programming Languages Overview",
    "description": "Detailed Overview of Programming Languages",
    "slug": "programming-languages",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
      {
        "name": "What Are Programming Languages?",
        "slug": "what-are-programming-languages",
      },
      {
        "name": "Popular Programming Languages",
        "slug": "popular-programming-languages",
      }
    ],
  },
  "data-strutures-and-algorithms":{
      "title": "Data Structures and Algorithms Overview",
    "description": "Detailed Overview of DSA and Coding Patterns",
    "slug": "data-strutures-and-algorithms",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
      {
        "name": "Overview of Data Structures",
        "slug": "overview-of-data-strutures",
      },
      {
        "name": "Overview of Algorithms",
        "slug": "overview-of-algorithms",
      },
      {
          "name": "Famous Coding Patterns",
          "slug": "famous-coding-patterns",
      }
    ],
  },
  "version-control":{
      "title": "Git and GitHub: A Comprehensive Guide",
    "description": "Detailed Overview of Git and Github",
    "slug": "version-control",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
       {
        "name": "Introduction to Version Control",
        "slug": "introduction-to-version-control"
        },
        {
            "name": "Common Git Commands",
            "slug": "common-git-commands"
        },
        {
            "name": "Advanced Git Topics",
            "slug": "advanced-git-topics"
        },
        {
            "name": "GitHub Overview",
            "slug": "github-overview"
        }
    ],
  },
  "databases":{
      "title": "Databases for Developement",
    "description": "Comprehensive Overview of Databases",
    "slug": "databases",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
        {
            "name": "Introduction to Databases",
            "slug": "introduction-to-databases"
        },
        {
            "name": "SQL Databases",
            "slug": "sql-databases"
        },
        {
            "name": "NoSQL Databases",
            "slug": "nosql-databases"
        },
        {
            "name": "SQL vs NoSQL",
            "slug": "sql-vs-nosql"
        }
    ],
  },
  "design-patterns":{
      "title": "Design Patterns Overview",
    "description": "Design Patterns Roadmap for Beginners",
    "slug": "design-patterns",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
        {
        "name": "Introduction to Design Patterns",
        "slug": "introduction-to-design-patterns"
        },
        {
            "name": "Types of Design Patterns",
            "slug": "types-of-design-patterns"
        },
        {
            "name": "Popular Design Patterns Explained",
            "slug": "popular-design-patterns-explained"
        },
        {
            "name": "Significance and Resources",
            "slug": "significance-and-resources"
        }
    ],
  },
  "web-frameworks":{
      "title": "Web Frameworks",
    "description": "Web Frameworks Backend Development Roadmap",
    "slug": "web-frameworks",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
        {
        "name": "Introduction to Web Frameworks",
        "slug": "introduction-to-web-frameworks"
        },
        {
            "name": "Types of Web Frameworks",
            "slug": "types-of-web-frameworks"
        },
        {
            "name": "Popular Backend Web Frameworks",
            "slug": "popular-backend-web-frameworks"
        },
        {
            "name": "Core Concepts",
            "slug": "core-concepts"
        },
        {
            "name": "Advanced Concepts",
            "slug": "advanced-concepts"
        },
        {
            "name": "Resources",
            "slug": "resources"
        }
    ],
  },
  "apis":{
      "title": "API Design",
    "description": "API Roadmap for Backend Development",
    "slug": "apis",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
        {
        "name": "Introduction to APIs",
        "slug": "introduction-to-apis"
        },
        {
            "name": "Introduction to GraphQL",
            "slug": "introduction-to-graphql"
        },
        {
            "name": "API Design Best Practices",
            "slug": "api-design-best-practices"
        },
        {
            "name": "API Roadmap: Beginner to Advanced",
            "slug": "api-roadmap-beginner-to-advanced"
        }
    ],
  },
  "micro-services":{
      "title": "Microservices Architecture",
    "description": "Microservices Architecture: Comprehensive Guide",
    "slug": "micro-services",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
        {
        "name": "Introduction to Microservices Architecture",
        "slug": "introduction-to-microservices-architecture"
        },
        {
            "name": "Why Use Microservices?",
            "slug": "why-use-microservices"
        },
        {
            "name": "Real World Use Cases",
            "slug": "real-world-use-cases"
        },
        {
            "name": "Core Components",
            "slug": "core-components"
        },
        {
            "name": "Go in Microservices",
            "slug": "go-in-microservices"
        },
        {
            "name": "Best Practices for Building Microservices",
            "slug": "best-practices-for-building-microservices"
        },
        {
            "name": "Resources",
            "slug": "resources"
        }
    ],
  }
}

def create_folders_and_files(data):
    for folder_name, folder_data in data.items():
        # Create the folder based on the key
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
       
        # Iterate through chapters and create files
        chapters = folder_data.get("chapters", [])
        for chapter in chapters:
            file_name = f"{chapter['slug']}.md"
            file_path = os.path.join(folder_name, file_name)
           
            # Create and write to the file with the required format
            with open(file_path, "w") as file:
                file_content = f"---\ntitle: \"{chapter['name']}\"\n---\n"  # Frontmatter format
                file.write(file_content)
                print(f"File '{file_name}' created in folder '{folder_name}'.")

# Call the function to execute the folder and file creation
create_folders_and_files(data)