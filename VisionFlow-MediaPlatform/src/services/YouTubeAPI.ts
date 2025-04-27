// Replace with your actual YouTube Data API key.
const API_KEY = "YOUR_YOUTUBE_API_KEY"; // Replace with your actual API key
const BASE_URL = "https://www.googleapis.com/youtube/v3/search";

// Global variable for pagination token. If it's empty (""), we are at the first page.
let nextPageToken = "";

/**
 * Searches YouTube videos based on the query.
 * @param query   The search keyword.
 * @param append  If true, appends the new videos to the existing ones.
 *                If false, clears the existing list and resets pagination.
 */
export function searchVideos(query: string, append = false) {
  const videoSection = document.getElementById("video-section");

  // If we're not appending, clear the section and reset the token.
  if (!append && videoSection) {
    videoSection.innerHTML = "";
    nextPageToken = "";
  }

  // Construct the request URL to query YouTube Data API.
  // We add &pageToken={nextPageToken} only if nextPageToken is non‐empty.
  let requestUrl = `${BASE_URL}?part=snippet&type=video&maxResults=5&q=${encodeURIComponent(
    query
  )}&key=${API_KEY}`;

  if (nextPageToken) {
    requestUrl += `&pageToken=${nextPageToken}`;
  }

  fetch(requestUrl)
    .then((response) => response.json())
    .then((data) => {
      if (!data.items || data.items.length === 0) {
        console.warn("No results found for:", query);
        return;
      }

      data.items.forEach((item: any) => {
        const videoElement = document.createElement("div");
        const videoId = item.id.videoId;
        const title = item.snippet.title;

        videoElement.innerHTML = `
          <h3>${title}</h3>
          <iframe 
            width="560" 
            height="315" 
            src="https://www.youtube.com/embed/${videoId}" 
            frameborder="0" 
            allowfullscreen>
          </iframe>
        `;
        videoSection?.appendChild(videoElement);
      });

      // If there's a nextPageToken, store it and show the "Load More" button.
      // Otherwise, reset the token and hide the button.
      if (data.nextPageToken) {
        nextPageToken = data.nextPageToken;
        const loadMoreBtn = document.getElementById("loadMoreBtn");
        if (loadMoreBtn) loadMoreBtn.style.display = "inline-flex";
      } else {
        nextPageToken = "";
        const loadMoreBtn = document.getElementById("loadMoreBtn");
        if (loadMoreBtn) loadMoreBtn.style.display = "none";
      }
    })
    .catch((error) => console.error("Error fetching YouTube videos:", error));
}

/**
 * Automatically searches for videos based on the last stored mood
 * (useful for personalized recommendations on page load).
 */
export function personalizedRecommendations() {
  const lastMood = localStorage.getItem("lastMood");
  if (lastMood) {
    searchVideos(lastMood);
  }
}

/**
 * Creates an auto‐play YouTube playlist based on the given query.
 * Uses "listType=search" to search for matching videos.
 */
export function autoPlayPlaylist(query: string) {
  const playlistSection = document.getElementById("playlist-section");
  if (!playlistSection) return;

  playlistSection.innerHTML = `
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed?listType=search&list=${encodeURIComponent(
        query
      )}"
      frameborder="0"
      allowfullscreen
    ></iframe>
  `;
}
