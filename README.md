An open-source software development tool to manage issues, sprints, and product roadmaps with peace of mind 🧘‍♀️.

> Plane is still in its early days, not everything will be perfect yet, and hiccups may happen. Please let us know of any suggestions, ideas, or bugs that you encounter on our Discord or GitHub issues, and we will use your feedback to improve on our upcoming releases.

The easiest way to get started with Plane is by creating a Plane Cloud account. Plane Cloud offers a hosted solution for Plane. If you prefer to self-host Plane, please refer to our deployment documentation. 

## ⚡️ Contributors Quick Start

### Prerequisite

Development system must have docker engine installed and running.

### Steps

Setting up local environment is extremely easy and straight forward. Follow the below step and you will be ready to contribute

1. Clone the code locally
1. Switch to the code folder `cd plane`
1. Create your feature or fix branch you plan to work on using `git checkout -b <feature-branch-name>`
1. Open terminal and run `./setup.sh`
1. Open the code on VSCode or similar equivalent IDE
1. Review the `.env` files available in various folders. Visit Environment Setup to know about various environment variables used in system
1. Run the docker command to initiate various services `docker compose -f docker-compose-local.yml up -d`

You are ready to make changes to the code. Do not forget to refresh the browser (in case id does not auto-reload)

Thats it!

## 🚀 Features

- **Issue Planning and Tracking**: Quickly create issues and add details using a powerful rich text editor that supports file uploads. Add sub-properties and references to issues for better organization and tracking.
- **Issue Attachments**: Collaborate effectively by attaching files to issues, making it easy for your team to find and share important project-related documents.
- **Layouts**: Customize your project view with your preferred layout - choose from List, Kanban, or Calendar to visualize your project in a way that makes sense to you.
- **Cycles**: Plan sprints with Cycles to keep your team on track and productive. Gain insights into your project's progress with burn-down charts and other useful features.
- **Modules**: Break down your large projects into smaller, more manageable modules. Assign modules between teams to easily track and plan your project's progress.
- **Views**: Create custom filters to display only the issues that matter to you. Save and share your filters in just a few clicks.
- **Pages**: Plane pages function as an AI-powered notepad, allowing you to easily document issues, cycle plans, and module details, and then synchronize them with your issues.
- **Command K**: Enjoy a better user experience with the new Command + K menu. Easily manage and navigate through your projects from one convenient location.
- **GitHub Sync**: Streamline your planning process by syncing your GitHub issues with Plane. Keep all your issues in one place for better tracking and collaboration.

