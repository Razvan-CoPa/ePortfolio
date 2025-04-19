import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/Contacts": {
        target: "https://67faadb68ee14a5426285900.mockapi.io",
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
