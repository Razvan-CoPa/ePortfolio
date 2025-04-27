(function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))d(e);new MutationObserver(e=>{for(const t of e)if(t.type==="childList")for(const l of t.addedNodes)l.tagName==="LINK"&&l.rel==="modulepreload"&&d(l)}).observe(document,{childList:!0,subtree:!0});function c(e){const t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),e.crossOrigin==="use-credentials"?t.credentials="include":e.crossOrigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function d(e){if(e.ep)return;e.ep=!0;const t=c(e);fetch(e.href,t)}})();const E="",I="https://www.googleapis.com/youtube/v3/search";let m="";function p(r,s=!1){const c=document.getElementById("video-section");!s&&c&&(c.innerHTML="",m="");let d=`${I}?part=snippet&type=video&maxResults=5&q=${encodeURIComponent(r)}&key=${E}`;m&&(d+=`&pageToken=${m}`),fetch(d).then(e=>e.json()).then(e=>{if(!e.items||e.items.length===0){console.warn("No results found for:",r);return}if(e.items.forEach(t=>{const l=document.createElement("div"),f=t.id.videoId,g=t.snippet.title;l.innerHTML=`
          <h3>${g}</h3>
          <iframe 
            width="560" 
            height="315" 
            src="https://www.youtube.com/embed/${f}" 
            frameborder="0" 
            allowfullscreen>
          </iframe>
        `,c==null||c.appendChild(l)}),e.nextPageToken){m=e.nextPageToken;const t=document.getElementById("loadMoreBtn");t&&(t.style.display="inline-flex")}else{m="";const t=document.getElementById("loadMoreBtn");t&&(t.style.display="none")}}).catch(e=>console.error("Error fetching YouTube videos:",e))}function v(){const r=localStorage.getItem("lastMood");r&&p(r)}function b(r){const s=document.getElementById("playlist-section");s&&(s.innerHTML=`
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed?listType=search&list=${encodeURIComponent(r)}"
      frameborder="0"
      allowfullscreen
    ></iframe>
  `)}function S(){return`
      <header>
          <h1>VisionFlow Dashboard</h1>
          <nav>
              <ul  class="nav_links">
                  <li><a href="index.html">Home</a></li>
                  <li><a href="about.html">About</a></li>
              </ul>
          </nav>
      </header>
  `}function B(){return`
      <label for="moodSelector">Select your mood:</label>
      <select id="moodSelector">
          <option value="Focus/Relaxation">Focus/Relaxation</option>
          <option value="Happy/Optimistic">Happy/Optimistic</option>
          <option value="Sad/Pessimistic">Sad/Pessimistic</option>
          <option value="Inspirational">Inspirational</option>
          <option value="Motivated">Motivated</option>
          <option value="Stressed">Stressed</option>
          <option value="Anxious">Anxious</option>
          <option value="Romantic">Romantic</option>
          <option value="Energetic">Energetic</option>
          <option value="Peaceful">Peaceful</option>
      </select>
  `}function w(){return`
      <button id="darkModeToggle">Toggle Dark Mode</button>
  `}function M(){var s,c,d,e,t,l,f;const r=document.getElementById("app");if(r){let g=function(){const o=localStorage.getItem("avatar"),n=document.getElementById("avatar-container");if(o&&n){n.innerHTML="";const i=document.createElement("img");i.src=o,i.alt="User Avatar",i.style.width="100px",i.style.height="100px",i.style.borderRadius="50%",n.appendChild(i)}};const y=localStorage.getItem("username")||"Guest";r.innerHTML=`
      ${S()}
      ${w()}
      <div id="user-profile-container">
          <h2>Welcome, ${y}</h2>
          <div id="avatar-container"></div>
          <p>Choose an image for your avatar:</p>
          <input type="file" id="avatarUpload" accept="image/*">
          
          <!-- Adăugăm input-ul pentru nume și butonul Save sub avatar: -->
          <input type="text" id="usernameInput" placeholder="Enter your name" />
          <button id="saveUsername">Save</button>
      </div>
      <main>
          ${B()}
          <input type="text" id="search" placeholder="Search for videos..." />
          <button id="searchBtn">Search</button>
          <button id="voiceCommandBtn">🎤 Voice Command</button>
          <section id="video-section"></section>
          <button id="loadMoreBtn" style="display: none;">Load More</button>
          <section id="recommendations-section"></section>
          <section id="playlist-section"></section>
      </main>
    `,(s=document.getElementById("searchBtn"))==null||s.addEventListener("click",()=>{const o=document.getElementById("search").value;p(o,!1)}),(c=document.getElementById("moodSelector"))==null||c.addEventListener("change",o=>{const n=o.target.value,a={"Sad/Pessimistic":"uplifting music for sadness","Focus/Relaxation":"calm study music","Happy/Optimistic":"energetic happy tunes",Inspirational:"inspirational background music",Motivated:"motivational workout music",Stressed:"stress relief music",Anxious:"anxiety calming music",Romantic:"romantic love songs",Energetic:"high energy dance music",Peaceful:"peaceful instrumental tracks"}[n]||"";if(a){const u=document.getElementById("search");u.value=a,p(a,!1),localStorage.setItem("lastMood",n),v(),b(a)}}),(d=document.getElementById("darkModeToggle"))==null||d.addEventListener("click",()=>{document.body.classList.toggle("dark-mode")}),(e=document.getElementById("voiceCommandBtn"))==null||e.addEventListener("click",()=>{const o=window.SpeechRecognition||window.webkitSpeechRecognition;if(o){const n=new o;n.lang="en-US",n.start(),n.onresult=i=>{const a=i.results[0][0].transcript.toLowerCase();if(a.includes("search")){const u=a.replace("search","").trim();p(u)}else if(a.includes("mood")){const u=a.replace("mood","").trim(),h=document.getElementById("moodSelector");h&&(h.value=u,h.dispatchEvent(new Event("change")))}},n.onerror=i=>{console.error("Speech recognition error:",i.error)}}else alert("Speech Recognition is not supported in this browser.")}),v(),(t=document.getElementById("avatarUpload"))==null||t.addEventListener("change",o=>{var i;const n=(i=o.target.files)==null?void 0:i[0];if(n){const a=new FileReader;a.onload=()=>{localStorage.setItem("avatar",a.result),g()},a.readAsDataURL(n)}}),g(),(l=document.getElementById("saveUsername"))==null||l.addEventListener("click",()=>{const o=document.getElementById("usernameInput");if(o.value){localStorage.setItem("username",o.value);const n=document.querySelector("#user-profile-container h2");n&&(n.textContent=`Welcome, ${o.value}`)}}),(f=document.getElementById("loadMoreBtn"))==null||f.addEventListener("click",()=>{const o=document.getElementById("search").value;p(o,!0)})}}M();
