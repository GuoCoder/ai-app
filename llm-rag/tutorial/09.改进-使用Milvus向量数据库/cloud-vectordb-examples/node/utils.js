export const isVersionAtLeast = (targetVersion, version) => {
  const targetParts = targetVersion.split(".").map(Number);
  const parts = version.split(".").map(Number);
  for (let i = 0; i < targetParts.length; i++) {
    if (parts[i] > targetParts[i]) {
      return true;
    } else if (parts[i] < targetParts[i]) {
      return false;
    }
  }
  return true;
};
