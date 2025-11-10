import { Outlet } from 'react-router-dom';
import Routes from './routes';
import { ThemeProvider } from './context/ThemeContext';
import { JSONProvider } from './context/JSONProvider';
import { AEIPProvider } from './context/AEIPContext';
import { LedgerProvider } from './context/LedgerContext';
import HeaderBar from './components/HeaderBar';
import FooterBar from './components/FooterBar';
import SideNav from './components/SideNav';
import { useFocusOutline } from './hooks/useFocusOutline';

function AppLayout() {
  useFocusOutline();
  return (
    <div className="app-shell" data-testid="app-shell">
      <HeaderBar />
      <div className="app-shell__body">
        <SideNav />
        <main id="main" className="app-shell__main" tabIndex={-1}>
          <Outlet />
        </main>
      </div>
      <FooterBar />
    </div>
  );
}

export default function App() {
  return (
    <ThemeProvider>
      <JSONProvider>
        <AEIPProvider>
          <LedgerProvider>
            <Routes layout={<AppLayout />} />
          </LedgerProvider>
        </AEIPProvider>
      </JSONProvider>
    </ThemeProvider>
  );
}
