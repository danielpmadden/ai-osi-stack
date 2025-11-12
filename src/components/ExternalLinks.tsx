export default function ExternalLinks() {
  const linkBaseClasses =
    "rounded-full border border-slate-500/40 bg-slate-800 px-3 py-1 text-xs font-semibold uppercase tracking-wide text-slate-100 transition hover:bg-slate-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-slate-300";

  return (
    <div className="flex flex-wrap items-center justify-end gap-2">
      <a
        href="https://YOUR_USERNAME.github.io/gov-control-tower"
        target="_blank"
        rel="noreferrer"
        className={linkBaseClasses}
      >
        Governance Control Tower
      </a>
      <a
        href="https://ai-osi-stack.vercel.app"
        target="_blank"
        rel="noreferrer"
        className={linkBaseClasses}
      >
        AI OSI Stack Docs
      </a>
    </div>
  );
}
