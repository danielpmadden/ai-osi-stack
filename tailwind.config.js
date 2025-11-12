/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        sidebar: "#111827",
        header: "#0f172a"
      }
    }
  },
  plugins: []
};
