import glossary from '../data/glossary.json';

export default function GlossaryDrawer() {
  return (
    <div className="page" aria-labelledby="glossary-heading">
      <h1 id="glossary-heading">Glossary</h1>
      <dl className="glossary">
        {(glossary as Array<{ term: string; definition: string }>).map((entry) => (
          <div key={entry.term} className="glossary__entry">
            <dt>{entry.term}</dt>
            <dd>{entry.definition}</dd>
          </div>
        ))}
      </dl>
    </div>
  );
}
