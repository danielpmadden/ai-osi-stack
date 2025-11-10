import { ReactNode } from 'react';
import { Routes as RouterRoutes, Route, Navigate } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import LayerMapView from './pages/LayerMapView';
import AEIPSimulator from './pages/AEIPSimulator';
import LedgerConsole from './pages/LedgerConsole';
import ArtifactGallery from './pages/ArtifactGallery';
import VersionTimeline from './pages/VersionTimeline';
import GlossaryDrawer from './pages/GlossaryDrawer';
import FeedbackPortal from './pages/FeedbackPortal';

interface Props {
  layout: ReactNode;
}

export default function Routes({ layout }: Props) {
  return (
    <RouterRoutes>
      <Route element={layout}>
        <Route index element={<Dashboard />} />
        <Route path="layers" element={<LayerMapView />} />
        <Route path="aeip" element={<AEIPSimulator />} />
        <Route path="ledger" element={<LedgerConsole />} />
        <Route path="artifacts" element={<ArtifactGallery />} />
        <Route path="timeline" element={<VersionTimeline />} />
        <Route path="glossary" element={<GlossaryDrawer />} />
        <Route path="feedback" element={<FeedbackPortal />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </RouterRoutes>
  );
}
