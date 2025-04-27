export function createVideoPlayer(videoId: string, title: string) {
  return `
      <div class="video-container">
          <h3>${title}</h3>
          <iframe src="https://www.youtube.com/embed/${videoId}" frameborder="0" allowfullscreen></iframe>
      </div>
  `;
}
