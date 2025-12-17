import { useEffect, useState } from "react";

type Props = {
  uid: string;
};

export default function DashboardViewer({ uid }: Props) {
  const [embedPath, setEmbedPath] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!uid) return;

    setEmbedPath(null);
    setError(null);

    fetch(`/api/grafana/embed/${uid}`)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch embed URL");
        return res.json();
      })
      .then((data) => {
        setEmbedPath(data.embedPath);
      })
      .catch(() => {
        setError("Failed to load dashboard");
      });
  }, [uid]);

  if (error) {
    return <div style={{ padding: 20, color: "red" }}>{error}</div>;
  }

  if (!embedPath) {
    return <div style={{ padding: 20 }}>Loading dashboard…</div>;
  }

  return (
    <iframe
      src={embedPath}
      style={{
        width: "100%",
        height: "100%",
        border: "none",
      }}
    />
  );
}
