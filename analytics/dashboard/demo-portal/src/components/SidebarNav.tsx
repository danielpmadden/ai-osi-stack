const SidebarNav = () => {
  return (
    <aside className="sidebar-nav">
      <div className="sidebar-logo">AI OSI Stack v5.0</div>
      <nav className="sidebar-links">
        <a href="#layers">Layers Overview</a>
        <a href="#ledger">Ledger Log</a>
        <a href="#about">About</a>
      </nav>
      <footer className="sidebar-footer">Demo prototype — not for production</footer>
    </aside>
  );
};

export default SidebarNav;
