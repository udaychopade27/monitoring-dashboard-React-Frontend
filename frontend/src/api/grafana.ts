export async function fetchDashboards() {
  const res = await fetch("/api/grafana/dashboards")
  return res.json()
}

export async function fetchEmbedUrl(uid: string) {
  const res = await fetch(`/api/grafana/embed/${uid}`)
  return res.json()
}
