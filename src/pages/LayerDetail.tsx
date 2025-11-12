import { useParams } from "react-router-dom";

export default function LayerDetail() {
  const { id } = useParams();

  return (
    <section className="space-y-4">
      <h1 className="text-2xl font-semibold">Layer details will load dynamically here.</h1>
      {id ? (
        <p className="text-slate-600 dark:text-slate-300">
          Currently viewing insights for layer: <span className="font-medium text-slate-900 dark:text-white">{id}</span>
        </p>
      ) : (
        <p className="text-slate-600 dark:text-slate-300">Select a layer to review its contextual information.</p>
      )}
    </section>
  );
}
