export default {
  appType: 'mpa',

  build: {
    sourcemap: true,
  },

  server: {
    port: 3000,
    strictPort: true,
  },

  resolve: {
    alias: {
      '@': '/src',
    }
  }
};
