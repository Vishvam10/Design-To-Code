import js from '@eslint/js'
import globals from 'globals'
import react from 'eslint-plugin-react'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'

export default [
    { ignores: ['dist'] },
    {
        files: ['**/*.{js,jsx}'],
        languageOptions: {
            ecmaVersion: 2020,
            globals: {
                ...globals.browser,
                // Add Jest globals (describe, test, expect, etc). This is
                // important since I'm not handling imports for .spec files in
                // the backend. DO NOT REMOVE THIS.
                jest: true,
                describe: true,
                test: true,
                expect: true,
                it: true,
                beforeEach: true,
                beforeAll: true,
                afterEach: true,
                afterAll: true,
            },
            parserOptions: {
                ecmaVersion: 'latest',
                ecmaFeatures: { jsx: true },
                sourceType: 'module',
            },
        },
        settings: { react: { version: '18.3' } },
        plugins: {
            react,
            'react-hooks': reactHooks,
            'react-refresh': reactRefresh,
        },
        rules: {
            ...js.configs.recommended.rules,
            ...react.configs.recommended.rules,
            ...react.configs['jsx-runtime'].rules,
            ...reactHooks.configs.recommended.rules,
            'react/jsx-no-target-blank': 'off',
            'react-refresh/only-export-components': [
                'warn',
                { allowConstantExport: true },
            ],
            'no-unused-vars': [
                'warn',
                { varsIgnorePattern: '^React$', argsIgnorePattern: '^_' },
            ],
            // Disable specific React linting rules
            'react/prop-types': 'off', // Disable prop-types validation
            'react/jsx-uses-react': 'off', // Disable usage of React import
            'react/react-in-jsx-scope': 'off', // Disable requirement for React in scope
            // You can add more rules to disable as needed
        },
    },
]
