# Configuration Files for typescript project

### .prettierrc

The Prettier configuration file defines the code formatting rules.

```json
{
  "tabWidth": 2,
  "useTabs": false,
  "printWidth": 80,
  "arrowParens": "avoid",
  "jsxSingleQuote": false,
  "singleQuote": true,
  "semi": false,
  "trailingComma": "es5",
  "importOrder": ["^@/(.*)$", "^[./]"],
  "importOrderSeparation": false,
  "importOrderSortSpecifiers": false,
  "ignore": ["node_modules"],
  "organizeImports": false,
  "proseWrap": "always",
  "quoteProps": "as-needed",
  "bracketSpacing": true,
  "jsxBracketSameLine": false
}
```

### eslint.config.js

The ESLint configuration file sets up linting rules for JavaScript and
TypeScript files.

```js
import globals from 'globals'
import pluginJs from '@eslint/js'
import tseslint from 'typescript-eslint'

/** @type {import('eslint').Linter.Config[]} */
export default [
  { files: ['**/*.{js,mjs,cjs,ts}'] },
  { languageOptions: { globals: globals.node } },
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      '@typescript-eslint/no-explicit-any': 'off',
    },
  },
]
```

### package.json

The package.json file defines the project's dependencies.

```json
{
  "name": "change-me",
  "private": true,
  "devDependencies": {
    "@types/bun": "latest"
  },
  "peerDependencies": {
    "typescript": "^5"
  }
}
```

### tsconfig.json

The TypeScript configuration file sets up the compiler options.

```json
{
  "compilerOptions": {
    "lib": ["ESNext", "DOM"],
    "target": "ESNext",
    "module": "ESNext",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noPropertyAccessFromIndexSignature": false,
    "noImplicitAny": false
  }
}
```

## License

This project is licensed under the MIT License.
