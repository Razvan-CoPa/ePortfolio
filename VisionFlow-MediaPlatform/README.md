# VisionFlow

🚀 VisionFlow 🎥
VisionFlow is a dynamic web application designed to provide personalized YouTube video recommendations based on the user's mood. Built using TypeScript, Vite, HTML, and CSS, the app integrates seamlessly with the YouTube API to deliver curated content for relaxation, motivation, focus, and more. 🌟

🎯 Features
🎭 Mood-Based Recommendations: Select your mood and get video suggestions tailored to uplift, relax, or motivate you.
🔍 Auto-Complete Search: Instantly search for videos with suggestions auto-filled based on your mood.
🔄 Load More Videos: Easily browse more content with the "Load More" button for endless discovery.
🎙️ Voice Command Integration: Search for videos or change moods using voice commands for hands-free navigation.
👤 User Profiles: Customize your profile with an avatar and track your video preferences.
🌗 Dark Mode Toggle: Switch between light and dark themes effortlessly.


🛠️ Tech Stack
Frontend: TypeScript, HTML, CSS
Build Tool: Vite
API: YouTube Data API



📂 Project Structure


![Screenshot 2025-02-06 164158](https://github.com/user-attachments/assets/6beaa384-db1b-4216-a5f1-a99546a4b48a)


![VisionFlow](https://github.com/user-attachments/assets/5c93510c-727f-46e7-9f03-b8f75f066de8)



![Screenshot 2025-02-08 133355](https://github.com/user-attachments/assets/7da9445e-a304-4cf6-9c1b-eb8579bbb790)



🚀 Getting Started

1. Clone the repository:
git clone https://github.com/AndersenAlexander/VisionFlow-FinalProjectTypeScript
cd VisionFlow

2. Install dependencies:
npm install

3. Run the application:
npm run dev

4. Build for production:
npm run build

🔑 API Configuration
Obtain a YouTube Data API key from Google Developers Console.
Replace 'YOUR_YOUTUBE_API_KEY' in YouTubeAPI.ts with your API key.


🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

📄 License
This project is licensed under the MIT License.

🛠️ How we organized this project
1. Project Background and Vision
I initiated and managed the development of a web application called VisionFlow, which offers users the ability to search for videos on YouTube, select music based on their mood, and benefit from voice recognition functionalities. The main goal was to build an intuitive and modern platform, with a focus on user experience and the integration of an external API (YouTube Data API).
As Team Lead, I supervised a group of 12 members including myself. The basic tasks were divided in a way that capitalized on the strengths of each specialist:
1. Front-end Development: 5 people, including UI/UX design and interaction implementation (HTML, CSS, TypeScript).
2. Back-end Integration / API: 2 people, responsible for the communication module with YouTube Data API, creating paging functions and managing the token for subsequent requests.
3. Testing and QA: 2 people, responsibilities for automated/manual testing, code quality analysis, bug reporting.
4. Documentation and DevOps: 1 person, who managed the project documentation, configured the build/deployment environments and ensured version consistency.
________________________________________
2. Coordination Role
2.1. Planning and Delegation
• Requirements Identification: We established, together with the team, the application specifications: YouTube search module, automatic playlist, “mood” selector, avatar upload, voice recognition, etc.
• Task Creation: We divided the tasks into tickets managed within a project management system (e.g. Jira, Trello). Each member was assigned tasks based on their competence.
• Deadline Setting: We estimated the time required for each module (e.g.: 3 days for integration with YouTube API, 3 days for testing, etc.) and monitored progress.
2.2. Review and Feedback
• Code Reviews: Before merging a branch into the main branch, I organized code review sessions. I checked if the code conventions, TypeScript standards were followed and if the logic met the initial requirements.
• Design/UI Feedback: I provided guidance to the front-end team on the design side, to maintain consistency of colors, sizes, layouts (e.g. red buttons, centered text, uniform input, etc.).
• Intermediate Testing: After completing a module, QA executed the planned tests and I centralized the bug reports, and I redirected the bug resolution to the responsible members.
2.3. Resource Coordination
• Technical Mentoring: I organized short training sessions and "knowledge-sharing" to ensure that all team members know how to use YouTube Data API, localStorage or voice recognition.
• Team Synchronization: During daily stand-up meetings, we discussed technical bottlenecks and each person’s progress, allocating additional resources if needed.
• Final Integration: Towards the end, we consolidated all components (Dashboard, MoodSelector, DarkMode, UserProfile) and validated the end-to-end functionality.
________________________________________
3. Technical Results and Contributions
1. Dashboard.ts Module
o Main author: 3 front-end members.
o Contributions: Implementation of the main interface, dynamic HTML loading, button events, text fields, voice command, page navigation logic.
2. YouTubeAPI.ts Module
o Main author: 1 back-end specialist + 1 testing helper.
o Contributions: searchVideos function for YouTube Data API call, nextPageToken handling for pagination, autoPlayPlaylist(query) for dynamic playlist generation.
3. Mood Selector and Dark Mode
o Lead authors: 1 front-end member + 1 QA (for intensive cross-browser compatibility testing).
o Contributions: Creating a mood dropdown, loading the associated query, saving the state in localStorage, light/dark mode with .dark-mode.
4. Design & CSS
o Lead authors: 2 front-end designers.
o Contributions: Finalizing the layout (header, profile container, buttons), color palette (red #ff0000, background #f4f4f4), hover states, responsive design for various resolutions.
5. Testing & QA
o Lead authors: 2 QA members.
o Contributions: Integrated testing sessions, discovering avatar loading errors, testing speech recognition in various browsers (Chrome, Edge), testing pagination on various searches.
6. DevOps and Documentation
o Main author: 1 dedicated person.
o Contributions: Build and deploy environment setup, version management, final documentation of YouTubeAPI module, endpoints and localStorage config.
________________________________________
4. Key Aspects in Team Management
• Transparency in communication: each member clearly understood their responsibilities and delivery deadlines.
• Collaboration: we encouraged peer-review, pairing programming between front-end and back-end, to ensure that the API requirements and input/output data were understood.
• Feedback-Based Adaptation: during the project, the requirements were adjusted (for example, the pagination mode with nextPageToken instead of a numeric offset). The team reacted quickly to these types of changes.
• Motivation and Support: we provided public recognition to members who completed their tasks on time and assisted with additional resources those who were experiencing difficulties.
________________________________________
5. Conclusions
Through the coordinated effort of the 12 team members, we delivered a functional web application that:
• Consumes data from an external service (YouTube Data API).
• Provides flexibility in search (manual, voice, by state/mood).
• Personalizes the experience by saving username and avatar.
• Improves UX with incremental loading (“Load More”) and a dark mode (Dark Mode).
In my role as coordinator, I managed the process of defining requirements, dividing tasks and ensuring team cohesion. The result is a modern prototype, which can be expanded and adapted later. The experience highlighted the importance of planning, feedback and agility in delivering a product on time that meets the set objectives and is enjoyable to use.
