import artifacts from '../data/artifacts.json';
import Panel from '../components/Panel';
import { formatVersionDate } from '../utils/versioning';

export default function ArtifactGallery() {
  return (
    <div className="page" aria-labelledby="artifact-heading">
      <h1 id="artifact-heading">Artifact Gallery</h1>
      <div className="page__grid">
        {(artifacts as Array<{ id: string; name: string; summary: string; updatedAt: string }>).map((artifact) => (
          <Panel key={artifact.id}>
            <h2>{artifact.name}</h2>
            <p>{artifact.summary}</p>
            <small>Updated {formatVersionDate(artifact.updatedAt)}</small>
          </Panel>
        ))}
      </div>
    </div>
  );
}
