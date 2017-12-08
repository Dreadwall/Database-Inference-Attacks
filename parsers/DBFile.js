class DBFile {

	constructor(fileName, templateString) {
		this.fileName = fileName;
		this.templateString = templateString;
		this.templateItems = this.parseTemplateString(templateString);
	}

	// 
	discoverObjects(s, templateItems) {
		for (let i = 0; i < s.length; i++) {

		}
	}

	// both returns and stores the template object from the template string
	parseTemplateString(s) {
		let templateItems = [];
		let build = [];
		let currChar;
		let lastChar;
		let type;

		for (let i = 0; i < s.length; i++) {
			currChar = s.charAt(i);
			if (currChar.match(/[ \f\r\t\v\u00a0\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000\ufeff]/)) currChar = '';
			lastChar = build[build.length - 1];

			if ((currChar == "%" && lastChar == "<") ||
				(currChar == ">" && lastChar == "%")) {
				build[build.length - 1] = '';

				type = (currChar == ">") ? 'attr' : 'fill';
				if (i != 1) templateItems.push([build.join(''), type]);
				build = [];
			}
			else if (i == s.length - 1) {
				build.push(currChar);
				templateItems.push([build.join(''), 'fill']);
				build = [];
			} else {
				build.push(currChar);
			}
		}

		return templateItems;
	}


}

// module.exports = DBFile;
let foo = new DBFile('', `<% name %> asdf <% bar %> asdf 
	asdf`);
console.log(foo.templateItems);