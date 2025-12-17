const BASE_URL = import.meta.env.VITE_BACKEND_BASE_URL;

export const getDashboardIframeUrl = () => {
  const uid = import.meta.env.VITE_DASHBOARD_UID;
  return `${BASE_URL}/api/grafana/d/${uid}?orgId=1&kiosk=tv&theme=dark`;
};
