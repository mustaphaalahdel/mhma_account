[العربية](README.ar.md)

# MHMA Account (`mhma_account`)

A lightweight Odoo 17 module that adds small but useful **Accounting** enhancements:
- Link and review **Stock Valuation Layers** directly from an Accounting Move (Journal Entry / Invoice).
- Broaden access to **Partner Accounting Properties** for bookkeepers (Account Users).
- (Optional) Provide extra Arabic translations for Odoo Accounting terms.

> Note: This is a custom module. Documentation format is inspired by OCA style.

## Table of contents
- [Overview](#overview)
- [Key features](#key-features)
- [Security](#security)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technical details](#technical-details)
- [Known limitations](#known-limitations)
- [Bug Tracker](#bug-tracker)
- [Credits](#credits)
- [Maintainers](#maintainers)
- [License](#license)

## Overview
`mhma_account` is designed for organizations using Odoo Accounting + Inventory valuation and needing better traceability between:
- accounting entries (`account.move`)
- stock valuation layers (`stock.valuation.layer`)

It also makes certain accounting properties on Contacts available to the **Accounting User** role where required by your process.

## Key features

### 1) Stock Valuation tab on Accounting Moves
Adds a new **"Stock Valuation"** page to the `account.move` form.

It contains:
- **Linked valuation layers list** (read-only):
  - Product
  - Quantity
  - Value
- **Selection field to attach existing valuation layers**:
  - A Many2many picker that lets you select existing `stock.valuation.layer` records.
  - On selection, the module automatically writes `account_move_id = current move` on the selected valuation layers.

This is useful for:
- Auditing valuation postings and investigating differences.
- Manually associating valuation layers with a journal entry where needed.

### 2) Partner Accounting Properties available to Account Users
Extends the Accounting Properties view on Contacts (`res.partner`) so that users in:
- **Accounting / Accountant** (`account.group_account_user`)
can access the **Accounting Entries** section (depending on other security rules in your database).

### 3) Optional Arabic translation patch (extra)
Includes an Arabic `.po` file located at:
- `mhma_account/i18n_extra/ar.po`

This file contains Arabic translations for the **core `account` module** strings (not only this custom module).
You may import it manually if you want improved/adjusted Arabic accounting terminology.

## Security
This module adds an access rule for:
- `stock.valuation.layer` (model from `stock_account`)

Granted to:
- **Accounting Manager** (`account.group_account_manager`)

Permissions:
- Read: ✅
- Write: ✅
- Create: ✅
- Delete: ❌ (blocked intentionally)

This is required in some environments to allow linking valuation layers from accounting.

## Installation
1. Copy `mhma_account` into your Odoo addons path.
2. Restart Odoo server.
3. Enable **Developer Mode**.
4. Go to **Apps → Update Apps List**.
5. Search for `MHMA Account` and click **Install**.

## Configuration
### User groups
- To view/link valuation layers comfortably:
  - Ensure the user has the required Accounting roles (especially **Accounting Manager** if you want write access to valuation layers).
- To access partner accounting properties as a bookkeeper:
  - Add the user to **Accounting / Accountant** (`account.group_account_user`).

### Optional: Import Arabic translation file
If you want to use `i18n_extra/ar.po`:
1. Go to **Settings → Translations → Import Translation** (wording may vary).
2. Select Language: **Arabic**
3. Choose the translation file: `mhma_account/i18n_extra/ar.po`
4. Select module: **account** (if the wizard asks)
5. Import.

## Usage
### Stock valuation linking
1. Open **Accounting → Journal Entries** (or invoices).
2. Open an existing `account.move`.
3. Go to the new **Stock Valuation** tab.
4. Review the linked valuation layers in the list.
5. Use **Select Stock Valuation Layers** to pick existing layers.
   - Once selected, they will be linked by setting their `account_move_id`.

### Partner accounting properties
1. Open **Contacts**.
2. Open a partner.
3. Go to the **Accounting** / **Accounting Properties** section.
4. Accounting Users should now be able to access the accounting entries group (per your DB security configuration).

## Technical details
- Model extension:
  - Inherits `account.move`
  - Adds:
    - `stock_valuation_ids`: One2many to `stock.valuation.layer` via `account_move_id`
    - `stock_valuation_select_ids`: Many2many selector to choose existing valuation layers
- Onchange behavior:
  - `@api.onchange('stock_valuation_select_ids')` performs a `write()` on selected valuation layers to set `account_move_id`.

## Known limitations
- The linking logic uses `move.id` inside an onchange:
  - If the move is not saved yet (no ID), linking will not work as expected.
- The onchange writes immediately to `stock.valuation.layer` records:
  - This persists even if you later discard the `account.move` form changes.
- `stock_valuation_select_ids` is not auto-cleared after linking (selection remains).

## Bug Tracker
Report issues and feature requests via GitHub Issues in this repository.

## Credits
### Author
- Mustapha Alahdel

## Maintainers
This module is maintained by **Mustapha Alahdel**.

## License
The license key is not explicitly defined in `__manifest__.py`.
It is recommended to add a clear license (e.g., LGPL-3 / OPL-1) to avoid ambiguity.
