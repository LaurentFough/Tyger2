const root = 'http://192.168.2.144:8000/';

export const Settings = {
    // Server configuration
    root: root,
    API: {
        LOGIN: root + 'api-token-auth/',
        REGISTER: root + 'user/register',
      }
};
window.settings = Settings;





