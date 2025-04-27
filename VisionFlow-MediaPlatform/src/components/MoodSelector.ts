// MoodSelector.ts

export function createMoodSelector() {
  return `
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
  `;
}
