import { Link } from 'react-router-dom';
import { t } from '../i18n';
import { useTheme } from '../hooks/useTheme';
import { useJSONContext } from '../context/JSONProvider';

export default function HeaderBar() {
  const { toggleTheme, theme } = useTheme();
  const { loading } = useJSONContext();

  return (
    <header className="header-bar" role="banner">
      <Link to="/" className="header-bar__title">
        {t('app.title')}
      </Link>
      <div className="header-bar__actions">
        <span aria-live="polite" className="header-bar__status">
          Docs {loading ? 'loading…' : 'synced'}
        </span>
        <button type="button" className="header-bar__theme" onClick={toggleTheme}>
          {theme === 'light' ? 'Dark mode' : 'Light mode'}
        </button>
      </div>
    </header>
  );
}
