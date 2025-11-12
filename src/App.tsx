import { Routes, Route } from "react-router-dom";
import GlobalLayout from "./layout/GlobalLayout";
import Overview from "./pages/Overview";
import LayerDetail from "./pages/LayerDetail";
import Frameworks from "./pages/Frameworks";
import AeipConfigurator from "./pages/AeipConfigurator";

export default function App() {
  return (
    <GlobalLayout>
      <Routes>
        <Route path="/" element={<Overview />} />
        <Route path="/layer/:id" element={<LayerDetail />} />
        <Route path="/frameworks" element={<Frameworks />} />
        <Route path="/aeip-config" element={<AeipConfigurator />} />
      </Routes>
    </GlobalLayout>
  );
}
