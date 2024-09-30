import os 
import json
data ={
  "jenkins-pipelines": {
    "title": "RealTime Jenkins Pipelines",
    "description": "Jenkins CICD pipelines used by top product companies",
    "slug": "jenkins-pipelines",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
    "chapters": [
      {
        "name": "Getting Started: The Basics of Jenkins Pipeline",
        "slug": "basics-of-jenkins",
      },
      {
        "name": "The Next Step: Jenkins Setup",
        "slug": "jenkins-setup",
      },
      {
        "name": "Integration of Tools: Drive the Jenkins Train",
        "slug": "tools-integration-with-Jenkins",
      },
      {
        "name": "Jenkinsfile with Groovy code: Groovy Analysis",
        "slug": "jenkins-groovy-code",
      },
      {
        "name": "Jenkins shared library: Integrate Jenkins with Parent child concept",
        "slug": "jenkins-shared-library",
      },
    ],
  },
  # "introduction-overview": {
  #   "title": "Introduction - Overview",
  #   "description": "Understanding Data Analysis and Data Analysts",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
  #   "slug": "introduction-overview",
  #   "chapters": [
  #     {
  #       "name": "What is Data Analysis?",
  #       "slug": "who-are-data-analysts",
  #     },
  #     {
  #       "name": "Who are Data Analysts?",
  #       "slug": "who-are-data-analysts",
  #     },
  #     {
  #       "name": "Types of Data Analyst Jobs in the Market",
  #       "slug": "types-of-data-analyst-jobs-in-the-market",
  #     },
  #     {
  #       "name": "Skills You Need to Become a Data Analyst in 2024: A Structured Approach",
  #       "slug": "skills-you-need-to-become-a-data-analyst-in-2024-a-structured-approach",
  #     },
  #   ],
  # },
  # "statistics-for-data-analytics": {
  #   "title": "Statistics for Data Analytics [Week 1-4]",
  #   "description": "Topics You Need to Learn in Statistics",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/statistics.png",
  #   "slug": "statistics-for-data-analytics",
  #   "chapters": [
  #     {
  #       "name": "Introduction: Why Statistics is Essential for Data Analysts",
  #       "slug": "introduction-why-statistics-is-essential-for-data-analysts",
  #     },
  #     {
  #       "name": "Descriptive Statistics [Week 1]",
  #       "slug": "descriptive-statistics-week-1",
  #     },
  #     {
  #       "name": "Probability Basics [Week 1]",
  #       "slug": "probability-basics-week-1",
  #     },
  #     {
  #       "name": "Inferential Statistics [Week 2]",
  #       "slug": "inferential-statistics-week-2",
  #     },
  #     {
  #       "name": "Correlation and Regression Analysis [Week 3]",
  #       "slug": "correlation-and-regression-analysis-week-3",
  #     },
  #     {
  #       "name": "Advanced Statistical Concepts [Week 4]",
  #       "slug": "advanced-statistical-concepts-week-4",
  #     },
  #     {
  #       "name": "A Structured Path to Learn Statistics",
  #       "slug": "a-structured-path-to-learn-statistics",
  #     },
  #     {
  #       "name": "Statistics Resources to Learn",
  #       "slug": "statistics-resources-to-learn",
  #     },
  #   ],
  # },
  # "sql": {
  #   "title": "SQL [Week 5-10]",
  #   "description": "SQL & Database Learning Roadmap: From Basics to Advanced",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/database.png",
  #   "slug": "sql",
  #   "chapters": [
  #     {
  #       "name": "Introduction to Databases [Week 5]",
  #       "slug": "introduction-to-databases-week-5",
  #     },
  #     {
  #       "name": "Introduction to SQL [Week 5]",
  #       "slug": "introduction-to-sql-week-5",
  #     },
  #     {
  #       "name": "SQL Commands [Week 6]",
  #       "slug": "sql-commands-week-6",
  #     },
  #     {
  #       "name": "Grouping, Aggregating, and Joins [Week 6]",
  #       "slug": "grouping-aggregating-and-joins-week-6",
  #     },
  #     {
  #       "name": "SQL Queries and Operators [Week 7]",
  #       "slug": "sql-queries-and-operators-week-7",
  #     },
  #     {
  #       "name": "Views, Indexes, and Performance Optimization [Week 8]",
  #       "slug": "views-indexes-and-performance-optimization-week-8",
  #     },
  #     {
  #       "name": "Advanced SQL Topics [Week 9]",
  #       "slug": "advanced-sql-topics-week-9",
  #     },
  #     {
  #       "name": "Putting Your SQL Knowledge to the Test [Week 10]",
  #       "slug": "putting-your-sql-knowledge-to-the-test-week-10",
  #     },
  #   ],
  # },
  # "python": {
  #   "title": "Python [Week 11-16]",
  #   "description": "Deep Dive into Python for Data Analysis",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/python.png",
  #   "slug": "python",
  #   "chapters": [
  #     {
  #       "name": "Python Basics [Week 11]",
  #       "slug": "python-basics-week-11",
  #     },
  #     {
  #       "name": "Data Structures in Python [Week 12]",
  #       "slug": "data-structures-in-python-week-12",
  #     },
  #     {
  #       "name": "File Handling and Data Input/Output [Week 13]",
  #       "slug": "file-handling-and-data-input-output-week-13",
  #     },
  #     {
  #       "name": "Introduction to Libraries for Data Analysis [Week 14]",
  #       "slug": "introduction-to-libraries-for-data-analysis-week-14",
  #     },
  #     {
  #       "name": "Data Visualization with Python [Week 15]",
  #       "slug": "data-visualization-with-python-week-15",
  #     },
  #     {
  #       "name": "Advanced Python for Data Analysis [Week 16]",
  #       "slug": "advanced-python-for-data-analysis-week-16",
  #     },
  #     {
  #       "name": "Automation and Scripting with Python [Week 16]-Optional",
  #       "slug": "automation-and-scripting-with-python-week-16-optional",
  #     },
  #     {
  #       "name": "How to Become a Pro in Python for Data Analysis: A Structured Path",
  #       "slug": "how-to-become-a-pro-in-python-for-data-analysis-a-structured-path",
  #     },
  #     {
  #       "name": "Python Resources to Learn and Practice [Week 11-16]",
  #       "slug": "python-resources-to-learn-and-practice-week-11-16",
  #     },
  #   ],
  # },

  # "ms-excel": {
  #   "title": "MS Excel [Week 17-18]",
  #   "description": "Complete Excel Roadmap to Become a Data Analyst",
  #   "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/excel.png",
  #   "slug": "ms-excel",
  #   "chapters": [
  #     {
  #       "name": "Introduction to Excel [Week 17]",
  #       "slug": "introduction-to-excel-week-17"
  #     },
  #     {
  #       "name": "Getting Started: Excel Basics [Week 17]",
  #       "slug": "getting-started-excel-basics-week-17"
  #     },
  #     {
  #       "name": "Intermediate Excel: Key Skills for Data Analysts [Week 17]",
  #       "slug": "intermediate-excel-key-skills-for-data-analysts-week-17"
  #     },
  #     {
  #       "name": "Advanced Excel: Mastering the Tools [Week 18]",
  #       "slug": "advanced-excel-mastering-the-tools-week-18"
  #     },
  #     {
  #       "name": "Automating Excel: Introduction to Macros & VBA [Week 18]",
  #       "slug": "automating-excel-introduction-to-macros-vba-week-18"
  #     },
  #     {
  #       "name": "Advanced Data Analysis Techniques [Week 18]",
  #       "slug": "advanced-data-analysis-techniques-week-18"
  #     },
  #     {
  #       "name": "Resources for Learning [Week 17 & 18]",
  #       "slug": "resources-for-learning-week-17-18"
  #     }
  #   ]
  # },
  # "analytics-tools": {
  #   "title": "Analytics Tools [Week 19-22]",
  #   "description": "Comprehensive Guide to Tableau and Power BI",
  #   "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/tools.png",
  #   "slug": "analytics-tools",
  #   "chapters": [
  #     {
  #       "name": "Introduction to Data Visualization Tools [Week 19]",
  #       "slug": "introduction-to-data-visualization-tools-week-19"
  #     },
  #     {
  #       "name": "Learning Path for Tableau [Week 19]",
  #       "slug": "learning-path-for-tableau-week-19"
  #     },
  #     {
  #       "name": "Detailed Tutorial Playlist [Week 19]",
  #       "slug": "detailed-tutorial-playlist-week-19"
  #     },
  #     {
  #       "name": "End to End Dashboarding Project for understanding [Week 20]",
  #       "slug": "end-to-end-dashboarding-project-for-understanding-week-20"
  #     },
  #     {
  #       "name": "Learning Path for Power BI [Week 21]",
  #       "slug": "learning-path-for-power-bi-week-21"
  #     },
  #     {
  #       "name": "Detailed Tutorial Playlist [Week 21]",
  #       "slug": "detailed-tutorial-playlist-week-21"
  #     },
  #     {
  #       "name": "End to End Dashboarding Project for understanding [Week 22]",
  #       "slug": "end-to-end-dashboarding-project-for-understanding-week-22"
  #     }
  #   ]
  # },
  # "data-analyst-projects": {
  #   "title": "Projects [Week 23-24]",
  #   "description": "End-To-End Guided Projects",
  #   "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/projects.png",
  #   "slug": "data-analyst-projects",
  #   "chapters": [
  #     {
  #       "name": "Power BI Dashboarding Projects [Week 23]",
  #       "slug": "power-bi-dashboarding-projects-week-23"
  #     },
  #     {
  #       "name": "Project Using Web Scraping, Python, Pandas and Power BI [Week 23]",
  #       "slug": "project-using-web-scraping-python-pandas-and-power-bi-week-23"
  #     },
  #     {
  #       "name": "Project using SQL & Power BI [Week 23]",
  #       "slug": "project-using-sql-power-bi-week-23"
  #     },
  #     {
  #       "name": "Tableau Dashboarding Projects [Week 24]",
  #       "slug": "tableau-dashboarding-projects-week-24"
  #     },
  #     {
  #       "name": "End to End Data Analytics Project (Python + SQL) [Week 24]",
  #       "slug": "end-to-end-data-analytics-project-python-sql-week-24"
  #     }
  #   ]
  # }
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
