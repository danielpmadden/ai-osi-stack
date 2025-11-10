import { NavLink } from 'react-router-dom';
import { t } from '../i18n';

const NAV_LINKS = [
  { to: '/', label: t('nav.dashboard'), end: true },
  { to: '/layers', label: t('nav.layers') },
  { to: '/aeip', label: t('nav.aeip') },
  { to: '/ledger', label: t('nav.ledger') },
  { to: '/artifacts', label: t('nav.artifacts') },
  { to: '/timeline', label: t('nav.timeline') },
  { to: '/glossary', label: t('nav.glossary') },
  { to: '/feedback', label: t('nav.feedback') }
];

export default function SideNav() {
  return (
    <nav className="side-nav" aria-label="Primary">
      <ul>
        {NAV_LINKS.map((link) => (
          <li key={link.to}>
            <NavLink
              to={link.to}
              end={link.end}
              className={({ isActive }) => (isActive ? 'side-nav__link side-nav__link--active' : 'side-nav__link')}
            >
              {link.label}
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  );
}
