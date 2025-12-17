import { useState } from "react";
import { DashboardList } from "./components/DashboardList";
import DashboardViewer from "./components/DashboardViewer";

export default function App() {
  const [selectedUid, setSelectedUid] = useState<string | null>(null);

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      <DashboardList onSelect={setSelectedUid} />

      <div style={{ flex: 1 }}>
        {selectedUid ? (
          <DashboardViewer uid={selectedUid} />
        ) : (
          <div style={{ padding: 20 }}>Select a dashboard</div>
        )}
      </div>
    </div>
  );
}
