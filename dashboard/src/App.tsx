import React from "react";
import { Dashboard } from "./pages/Dashboard";
import { SkipLink } from "./utils/accessibility";
import { useFocusOutline } from "./utils/accessibility";

export const App: React.FC = () => {
  useFocusOutline();

  return (
    <>
      <SkipLink href="#main-content" />
      <Dashboard />
    </>
  );
};

export default App;
