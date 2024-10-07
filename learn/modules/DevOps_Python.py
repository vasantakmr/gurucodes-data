import os 
import json
data = {
  # "jenkins-pipelines": {
  #   "title": "RealTime Jenkins Pipelines",
  #   "description": "Jenkins CICD pipelines used by top product companies",
  #   "slug": "jenkins-pipelines",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-roadmap.png",
  #   "chapters": [
  #     {
  #       "name": "Getting Started: The Basics of Jenkins Pipeline",
  #       "slug": "basics-of-jenkins",
  #     },
  #     {
  #       "name": "The Next Step: Jenkins Setup",
  #       "slug": "jenkins-setup",
  #     },
  #     {
  #       "name": "Integration of Tools: Drive the Jenkins Train",
  #       "slug": "tools-integration-with-Jenkins",
  #     },
  #     {
  #       "name": "Jenkinsfile with Groovy code: Groovy Analysis",
  #       "slug": "jenkins-groovy-code",
  #     },
  #     {
  #       "name": "Jenkins shared library: Integrate Jenkins with Parent child concept",
  #       "slug": "jenkins-shared-library",
  #     },
  #   ],
  # },
  # "linux-overview": {
  #   "title": "Linux: Overview",
  #   "description": "Understanding Linux from Basics",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
  #   "slug": "linux-Overview",
  #   "chapters": [
  #     {
  #       "name": "Linux Advanced Commands",
  #       "slug": "linux-in-devops",
  #     },
  #     {
  #       "name": "Linux Basic Commands",
  #       "slug": "linux-commands",
  #     },
  #     {
  #       "name": "Linux and DevOps:Interview Questions",
  #       "slug": "linux-devops-interview-qna",
  #     },
  #   ],
  # },
  # "docker-for-devops": {
  #   "title": "Docker for DevOps Engineers",
  #   "description": "Topics You Need to Learn in DevOps",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/statistics.png",
  #   "slug": "docker-for-devops",
  #   "chapters": [
  #     {
  #       "name": "Introduction: Why to learn Docker",
  #       "slug": "learn-docker-basics",
  #     },
  #     {
  #       "name": "Docker Architecture",
  #       "slug": "docker-architecture",
  #     },
  #     {
  #       "name": "Docker Images and Containers",
  #       "slug": "docker-images-containers",
  #     },
  #     {
  #       "name": "Dockerfile Setup",
  #       "slug": "dockerfile-overview",
  #     },
  #     {
  #       "name": "Docker commands indepth",
  #       "slug": "docker-commands-indepth",
  #     },
  #     {
  #       "name": "docker networking",
  #       "slug": "docker-networking",
  #     },
  #     {
  #       "name": "multistage dockerfile",
  #       "slug": "multistage-dockerfiles",
  #     },
  #     {
  #       "name": "dockerfile scenarios",
  #       "slug": "dockerfile-scenarios",
  #     },
  #   ],
  # },
  # "git": {
  #   "title": "Git for DevOps Engineers",
  #   "description": "learn Git from this flow: From Basics to Advanced",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/database.png",
  #   "slug": "git",
  #   "chapters": [
  #     {
  #       "name": "Introduction to Git",
  #       "slug": "git-introduction",
  #     },
  #     {
  #       "name": "Git Commands",
  #       "slug": "git-commands",
  #     },
  #     {
  #       "name": "Git Branching Startegy",
  #       "slug": "git-branching-strategy",
  #     },
  #     {
  #       "name": "git setup handson",
  #       "slug": "git-handson",
  #     },
  #     {
  #       "name": "git advanced concepts",
  #       "slug": "git-advanced-concepts",
  #     }
  #   ],
  # },
  # "kubernetes": {
  #   "title": "Kubernetes for DevOps Engineers",
  #   "description": "Kubernetes: From Basics to Advanced",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/database.png",
  #   "slug": "kubernetes",
  #   "chapters": [
  #     {
  #       "name": "kubernetes Architecture",
  #       "slug": "kubernetes-architecture",
  #     },
  #     {
  #       "name": "kubernetes commands",
  #       "slug": "kubernetes-commands",
  #     },
  #     {
  #       "name": "istio setup in kubernetes",
  #       "slug": "kubernetes-istio",
  #     },
  #     {
  #       "name": "kubernetes questions",
  #       "slug": "kubernetes-questions",
  #     },
  #     {
  #       "name": "kubernetes Resources:A to Z of KIND",
  #       "slug": "kubernetes-resources",
  #     },
  #     {
  #       "name": "kubernetes Cluster Upgrade",
  #       "slug": "kubernetes-cluster-upgrade",
  #     },
  #     {
  #       "name": "kubernetes interview questions",
  #       "slug": "kubernetes-interview-questions",
  #     },
  #     {
  #       "name": "kubernetes ingress",
  #       "slug": "kubernetes-ingress",
  #     },      
  #   ],
  # },
  #   "Ansible": {
  #   "title": "Ansible for DevOps Engineers",
  #   "description": "Ansible: From Basics to Advanced",
  #   "image":
  #     "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/database.png",
  #   "slug": "Ansible",
  #   "chapters": [
  #     {
  #       "name": "Ansible Introduction",
  #       "slug": "ansible-introduction",
  #     },
  #     {
  #       "name": "ansible adhoc commands",
  #       "slug": "ansible-adhoc-commands",
  #     },
  #     {
  #       "name": "ansible setup and playbooks",
  #       "slug": "ansible-playbooks",
  #     },
  #     {
  #       "name": "ansible roles",
  #       "slug": "ansible-roles",
  #     },
  #     {
  #       "name": "ansible:A to Z of automations",
  #       "slug": "ansible-automations",
  #     },
  #     {
  #       "name": "ansible handlers & notifiers",
  #       "slug": "ansible-handlers-notifiers",
  #     },
  #     {
  #       "name": "Ansible interview questions",
  #       "slug": "ansible-interview-questions",
  #     }   
  #   ],
  # }
    "terraform": {
    "title": "Terraform for DevOps Engineers",
    "description": "Terraform: From Basics to Advanced",
    "image":
      "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/database.png",
    "slug": "terraform",
    "chapters": [
      {
        "name": "terraform Introduction",
        "slug": "terraform-introduction",
      },
      {
        "name": "terraform commands",
        "slug": "terraform-commands",
      },
      {
        "name": "terraform setup",
        "slug": "terraform-setup",
      },
      {
        "name": "terraform code",
        "slug": "terraform-code",
      },
      {
        "name": "terraform provisioners",
        "slug": "terraform-provisioners",
      },
      {
        "name": "terraform modules",
        "slug": "terraform-modules",
      },
      {
        "name": "terraform state file",
        "slug": "terraform-state-file",
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
