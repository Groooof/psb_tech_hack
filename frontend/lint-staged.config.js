// eslint-disable-next-line no-undef
module.exports = {
	// Check TS files for no errors
	'**/*.(ts|tsx)': () => 'tsc --noEmit',

	// Lint and format TS and JS files
	'**/*.(ts|tsx|js)': (filenames) => [
		`npx eslint --fix ${filenames.join(' ')}`,
		`npx prettier --write ${filenames.join(' ')}`,
	],
};
