import { useEffect, useMemo, useState } from 'react';
import axios from 'axios';

const STATUS_COLORS = {
  green: '#16a34a',
  amber: '#f59e0b',
  red: '#dc2626'
};

function StatusPill({ status }) {
  const color = STATUS_COLORS[status] || '#64748b';
  return (
    <span className="status-indicator">
      <span className="status-dot" style={{ backgroundColor: color }} />
      {status?.toUpperCase() || 'UNKNOWN'}
    </span>
  );
}

function ArtifactCard({ title, outstanding, templatePath, status }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <StatusPill status={status} />
      <p>{outstanding.length ? `${outstanding.length} asset(s) missing this artifact.` : 'All evidence submitted.'}</p>
      <div className="actions">
        <a href={`/schemas/${templatePath}`} download>
          <button>Download template</button>
        </a>
      </div>
      {outstanding.length > 0 && (
        <ul>
          {outstanding.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

function RegistrationForm({ onRegister, isSubmitting }) {
  const [form, setForm] = useState({
    asset_id: '',
    name: '',
    type: 'model',
    owner: ''
  });

  const isValid = form.asset_id && form.name && form.owner;

  const submit = async (event) => {
    event.preventDefault();
    if (!isValid) return;
    await onRegister(form);
    setForm({ asset_id: '', name: '', type: 'model', owner: '' });
  };

  return (
    <form className="card" onSubmit={submit}>
      <h3>Register new artifact</h3>
      <label>
        Asset ID
        <input
          value={form.asset_id}
          onChange={(event) => setForm({ ...form, asset_id: event.target.value })}
          required
        />
      </label>
      <label>
        Name
        <input value={form.name} onChange={(event) => setForm({ ...form, name: event.target.value })} required />
      </label>
      <label>
        Type
        <select value={form.type} onChange={(event) => setForm({ ...form, type: event.target.value })}>
          <option value="model">Model</option>
          <option value="dataset">Dataset</option>
          <option value="asset">Asset</option>
        </select>
      </label>
      <label>
        Owner
        <input value={form.owner} onChange={(event) => setForm({ ...form, owner: event.target.value })} required />
      </label>
      <button type="submit" disabled={!isValid || isSubmitting}>
        {isSubmitting ? 'Registering…' : 'Register'}
      </button>
    </form>
  );
}

export default function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [items, setItems] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [registering, setRegistering] = useState(false);

  const refresh = async () => {
    setLoading(true);
    setError('');
    try {
      const [{ data: assets }, { data: metricsData }] = await Promise.all([
        axios.get('/api/assets'),
        axios.get('/api/metrics')
      ]);
      setItems(assets);
      setMetrics(metricsData);
    } catch (err) {
      setError(err.message || 'Failed to load governance data');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    refresh();
  }, []);

  const outstandingByArtifact = useMemo(() => {
    const map = new Map();
    items.forEach((item) => {
      item.missing_artifacts.forEach((artifact) => {
        if (!map.has(artifact)) {
          map.set(artifact, []);
        }
        map.get(artifact).push(item.asset_id);
      });
    });
    return map;
  }, [items]);

  const artifactStatus = (artifactName) => {
    const affected = items.filter((item) => item.missing_artifacts.includes(artifactName));
    if (affected.length === 0) {
      return 'green';
    }
    const hasRed = affected.some((item) => item.status === 'red');
    return hasRed ? 'red' : 'amber';
  };

  const artifactConfig = [
    { name: 'ModelCard', template: 'modelcard.template.yaml' },
    { name: 'CCM', template: 'ccm.template.yaml' },
    { name: 'IR', template: 'ir.template.yaml' },
    { name: 'AEIP', template: 'aeip.template.yaml' },
    { name: 'GDS', template: 'gds.template.yaml' }
  ];

  const registerAsset = async (payload) => {
    setRegistering(true);
    try {
      await axios.post('/api/assets', payload);
      await refresh();
    } finally {
      setRegistering(false);
    }
  };

  if (loading) {
    return (
      <div className="app-container">
        <p>Loading governance posture…</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app-container">
        <p role="alert">{error}</p>
      </div>
    );
  }

  return (
    <div className="app-container">
      <header>
        <div>
          <h1>Governance Control Tower</h1>
          <p>Compliance telemetry, ownership accountability, and actionable debt.</p>
        </div>
        {metrics && (
          <div className="card" style={{ minWidth: '260px' }}>
            <h3>Key Metrics</h3>
            <ul>
              {Object.entries(metrics.values || {}).map(([key, value]) => (
                <li key={key}>
                  <strong>{key}:</strong> {(value * 100).toFixed(1)}%
                </li>
              ))}
            </ul>
          </div>
        )}
      </header>

      <div className="dashboard-grid">
        <RegistrationForm onRegister={registerAsset} isSubmitting={registering} />
        {artifactConfig.map(({ name, template }) => (
          <ArtifactCard
            key={name}
            title={name}
            outstanding={outstandingByArtifact.get(name) || []}
            templatePath={template}
            status={artifactStatus(name)}
          />
        ))}
      </div>

      <section className="card" style={{ marginTop: '2rem' }}>
        <h2>Registered Artifacts</h2>
        <table className="table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Type</th>
              <th>Status</th>
              <th>Missing artifacts</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item) => (
              <tr key={item.asset_id}>
                <td>{item.asset_id}</td>
                <td>{item.name}</td>
                <td>
                  <span className="badge">{item.type}</span>
                </td>
                <td>
                  <StatusPill status={item.status} />
                </td>
                <td>{item.missing_artifacts.length ? item.missing_artifacts.join(', ') : 'None'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
}
