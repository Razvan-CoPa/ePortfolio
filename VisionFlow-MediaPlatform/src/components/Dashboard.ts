// Dashboard.ts

import {
  searchVideos,
  personalizedRecommendations,
  autoPlayPlaylist,
} from "../services/YouTubeAPI";
import { createHeader } from "./Header";
import { createMoodSelector } from "./MoodSelector";
import { createDarkModeToggle } from "./DarkModeToggle";

let currentPage = 1;

export function createApp() {
  const app = document.getElementById("app");
  if (app) {
    // Luăm username‐ul din localStorage (sau „Guest” dacă nu există)
    const storedUsername = localStorage.getItem("username") || "Guest";

    app.innerHTML = `
      ${createHeader()}
      ${createDarkModeToggle()}
      <div id="user-profile-container">
          <h2>Welcome, ${storedUsername}</h2>
          <div id="avatar-container"></div>
          <p>Choose an image for your avatar:</p>
          <input type="file" id="avatarUpload" accept="image/*">
          
          <!-- Adăugăm input-ul pentru nume și butonul Save sub avatar: -->
          <input type="text" id="usernameInput" placeholder="Enter your name" />
          <button id="saveUsername">Save</button>
      </div>
      <main>
          ${createMoodSelector()}
          <input type="text" id="search" placeholder="Search for videos..." />
          <button id="searchBtn">Search</button>
          <button id="voiceCommandBtn">🎤 Voice Command</button>
          <section id="video-section"></section>
          <button id="loadMoreBtn" style="display: none;">Load More</button>
          <section id="recommendations-section"></section>
          <section id="playlist-section"></section>
      </main>
    `;

    // Când dăm click pe Search:
    document.getElementById("searchBtn")?.addEventListener("click", () => {
      const query = (document.getElementById("search") as HTMLInputElement).value;
      currentPage = 1;
      searchVideos(query, false);
    });

    // Selectăm mood-ul din dropdown
    document
      .getElementById("moodSelector")
      ?.addEventListener("change", (event) => {
        const mood = (event.target as HTMLSelectElement).value;
        const moodMap: { [key: string]: string } = {
          "Sad/Pessimistic": "uplifting music for sadness",
          "Focus/Relaxation": "calm study music",
          "Happy/Optimistic": "energetic happy tunes",
          Inspirational: "inspirational background music",
          Motivated: "motivational workout music",
          Stressed: "stress relief music",
          Anxious: "anxiety calming music",
          Romantic: "romantic love songs",
          Energetic: "high energy dance music",
          Peaceful: "peaceful instrumental tracks",
        };

        const query = moodMap[mood] || "";
        if (query) {
          const searchInput = document.getElementById(
            "search"
          ) as HTMLInputElement;
          searchInput.value = query;
          currentPage = 1;
          searchVideos(query, false);
          localStorage.setItem("lastMood", mood);
          personalizedRecommendations();
          autoPlayPlaylist(query);
        }
      });

    // Activare Dark Mode
    document.getElementById("darkModeToggle")?.addEventListener("click", () => {
      document.body.classList.toggle("dark-mode");
    });

    // Voice command
    document
      .getElementById("voiceCommandBtn")
      ?.addEventListener("click", () => {
        const SpeechRecognition =
          window.SpeechRecognition || (window as any).webkitSpeechRecognition;
        if (SpeechRecognition) {
          const recognition = new SpeechRecognition();
          recognition.lang = "en-US";
          recognition.start();

          recognition.onresult = (event: any) => {
            const command = event.results[0][0].transcript.toLowerCase();
            if (command.includes("search")) {
              const query = command.replace("search", "").trim();
              searchVideos(query);
            } else if (command.includes("mood")) {
              const mood = command.replace("mood", "").trim();
              const moodSelector = document.getElementById(
                "moodSelector"
              ) as HTMLSelectElement;
              if (moodSelector) {
                moodSelector.value = mood;
                moodSelector.dispatchEvent(new Event("change"));
              }
            }
          };

          recognition.onerror = (event: any) => {
            console.error("Speech recognition error:", event.error);
          };
        } else {
          alert("Speech Recognition is not supported in this browser.");
        }
      });

    // Recomandări personalizate (dacă aveam ultimul mood salvat)
    personalizedRecommendations();

    // Upload avatar
    document
      .getElementById("avatarUpload")
      ?.addEventListener("change", (event) => {
        const file = (event.target as HTMLInputElement).files?.[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = () => {
            localStorage.setItem("avatar", reader.result as string);
            displayAvatar();
          };
          reader.readAsDataURL(file);
        }
      });

    function displayAvatar() {
      const avatarData = localStorage.getItem("avatar");
      const avatarContainer = document.getElementById("avatar-container");
      if (avatarData && avatarContainer) {
        avatarContainer.innerHTML = "";
        const avatarImage = document.createElement("img");
        avatarImage.src = avatarData;
        avatarImage.alt = "User Avatar";
        avatarImage.style.width = "100px";
        avatarImage.style.height = "100px";
        avatarImage.style.borderRadius = "50%";
        avatarContainer.appendChild(avatarImage);
      }
    }
    displayAvatar();

    // Salvare username
    document.getElementById("saveUsername")?.addEventListener("click", () => {
      const usernameInput = document.getElementById(
        "usernameInput"
      ) as HTMLInputElement;
      if (usernameInput.value) {
        localStorage.setItem("username", usernameInput.value);

        // Actualizăm instant textul din <h2> (fără a mai da reload)
        const h2Element = document.querySelector("#user-profile-container h2");
        if (h2Element) {
          h2Element.textContent = `Welcome, ${usernameInput.value}`;
        }
      }
    });

    // Load More
    document.getElementById("loadMoreBtn")?.addEventListener("click", () => {
      const query = (document.getElementById("search") as HTMLInputElement)
        .value;
      currentPage++;
      searchVideos(query, true, currentPage);
    });
  }
}
