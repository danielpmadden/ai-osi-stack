import Panel from '../components/Panel';
import { useFeedback } from '../hooks/useFeedback';

export default function FeedbackPortal() {
  const { entries, loading } = useFeedback();
  return (
    <div className="page" aria-labelledby="feedback-heading">
      <h1 id="feedback-heading">Civic Feedback</h1>
      {loading ? <p role="status">Loading civic feedback…</p> : null}
      <div className="page__grid">
        {entries.map((entry) => (
          <Panel key={entry.id}>
            <h2>{entry.source}</h2>
            <p>{entry.message}</p>
            <small>Submitted {new Date(entry.submittedAt).toLocaleDateString()}</small>
          </Panel>
        ))}
      </div>
    </div>
  );
}
