import plans from '../data/update_plans.json';
import Panel from '../components/Panel';

export default function VersionTimeline() {
  return (
    <div className="page" aria-labelledby="timeline-heading">
      <h1 id="timeline-heading">Version Timeline</h1>
      <ol className="timeline">
        {(plans as Array<{ id: string; title: string; milestones: string[]; status: string }>).map((plan) => (
          <li key={plan.id}>
            <Panel>
              <h2>{plan.title}</h2>
              <p>Status: {plan.status}</p>
              <ul>
                {plan.milestones.map((step) => (
                  <li key={step}>{step}</li>
                ))}
              </ul>
            </Panel>
          </li>
        ))}
      </ol>
    </div>
  );
}
