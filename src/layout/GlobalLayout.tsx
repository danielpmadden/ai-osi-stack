import { PropsWithChildren, useEffect, useMemo, useState } from "react";
import { Link, NavLink, useLocation } from "react-router-dom";

import ExternalLinks from "../components/ExternalLinks";

const navItems = [
  { label: "Overview", to: "/" },
  { label: "Layers", to: "/layer/core" },
  { label: "Frameworks", to: "/frameworks" },
  { label: "AEIP Config", to: "/aeip-config" }
];

export default function GlobalLayout({ children }: PropsWithChildren) {
  const [isDark, setIsDark] = useState(() =>
    typeof window !== "undefined" ? document.documentElement.classList.contains("dark") : false
  );
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const location = useLocation();

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add("dark");
      document.documentElement.style.colorScheme = "dark";
    } else {
      document.documentElement.classList.remove("dark");
      document.documentElement.style.colorScheme = "light";
    }
  }, [isDark]);

  useEffect(() => {
    setSidebarOpen(false);
  }, [location.pathname]);

  const headerNav = useMemo(() => navItems.slice(1), []);

  return (
    <div className="layout bg-slate-100 text-slate-900 dark:bg-slate-900 dark:text-slate-100">
      <header className="flex h-[var(--header-height)] items-center justify-between border-b border-slate-200 bg-header px-4 text-white shadow-sm dark:border-slate-700 md:px-6">
        <div className="flex items-center gap-3">
          <button
            type="button"
            className="inline-flex items-center justify-center rounded-lg bg-slate-800 px-3 py-1 text-sm font-medium uppercase tracking-wide text-slate-100 shadow hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-slate-400"
          >
            AI
          </button>
          <Link to="/" className="text-lg font-semibold">
            AI OSI Stack
          </Link>
        </div>
        <div className="flex items-center gap-3 md:gap-4">
          <button
            type="button"
            className="inline-flex items-center justify-center rounded-md border border-slate-500/50 bg-slate-800 p-2 text-lg text-slate-100 shadow hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-slate-300 md:hidden"
            aria-label="Toggle navigation"
            onClick={() => setSidebarOpen((prev) => !prev)}
          >
            ☰
          </button>
          <nav className="hidden items-center gap-2 md:flex">
            {headerNav.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  `rounded-md px-3 py-2 text-sm font-medium transition-colors ${
                    isActive ? "bg-slate-200/20 text-white" : "text-slate-200 hover:bg-slate-200/10"
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
          <ExternalLinks />
          <button
            type="button"
            onClick={() => setIsDark((prev) => !prev)}
            className="flex items-center gap-2 rounded-md border border-slate-500/50 bg-slate-800 px-3 py-2 text-sm font-semibold text-slate-100 shadow hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-slate-300"
            aria-label="Toggle theme"
          >
            <span className="hidden md:inline">{isDark ? "Dark" : "Light"} mode</span>
            <span aria-hidden>{isDark ? "🌙" : "☀️"}</span>
          </button>
        </div>
      </header>
      <aside
        className={`flex flex-col gap-6 border-r border-slate-800/30 bg-sidebar p-6 transition-transform duration-300 md:translate-x-0 ${
          sidebarOpen ? "translate-x-0" : "-translate-x-full"
        } md:static md:flex`}
      >
        <div>
          <p className="text-xs uppercase tracking-widest text-slate-400">Navigation</p>
        </div>
        <nav className="space-y-2">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `block rounded-lg px-4 py-2 text-sm font-medium transition-colors ${
                  isActive
                    ? "bg-slate-100/10 text-white shadow-lg"
                    : "text-slate-200 hover:bg-slate-100/10 hover:text-white"
                }`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>
      {sidebarOpen && (
        <button
          type="button"
          aria-label="Close navigation"
          onClick={() => setSidebarOpen(false)}
          className="fixed inset-0 z-10 block bg-black/40 backdrop-blur-sm md:hidden"
        />
      )}
      <main className="relative z-0 bg-white text-slate-900 shadow-inner dark:bg-slate-950 dark:text-slate-100">
        {children}
      </main>
    </div>
  );
}
