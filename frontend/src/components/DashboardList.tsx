import { useEffect, useState } from "react"
import { fetchDashboards } from "../api/grafana"

export function DashboardList({ onSelect }: { onSelect: (uid: string) => void }) {
  const [dashboards, setDashboards] = useState<any[]>([])

  useEffect(() => {
    fetchDashboards().then(setDashboards)
  }, [])

  return (
    <ul>
      {dashboards.map(d => (
        <li key={d.uid}>
          <button onClick={() => onSelect(d.uid)}>
            {d.title}
          </button>
        </li>
      ))}
    </ul>
  )
}
