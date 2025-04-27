export function createUserProfile() {
  const username = localStorage.getItem("username") || "Guest";
  return `
      <section id="user-profile">
          <h2>Welcome, ${username}</h2>
          <input type="text" id="usernameInput" placeholder="Enter your name" />
          <button id="saveUsername">Save</button>
      </section>
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("saveUsername")?.addEventListener("click", () => {
    const username = (
      document.getElementById("usernameInput") as HTMLInputElement
    ).value;
    if (username) {
      localStorage.setItem("username", username);
      location.reload();
    }
  });
});
