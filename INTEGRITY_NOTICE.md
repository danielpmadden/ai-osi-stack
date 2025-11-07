---
canonical_version: "AI OSI Stack v5"
canonical_date: "2025-11-07"
aeip_version: "1.3"
repository_of_record: "https://github.com/danielpmadden/ai-osi-stack"
domain_of_record: "https://aiosi.org"
supersedes_all_prior_metadata: true
---

# Integrity Notice — AI OSI Stack v5

This notice anchors the canonical public record for AI OSI Stack v5. Verify the repository state, release artifacts, and AEIP payloads before relying on any derivative work.

## Required Checksums (SHA-512)
| Artifact | Path | SHA-512 |
| --- | --- | --- |
| Canonical PDF | `versions/ai-osi-stack-v5.pdf` | `87d0414872ab29393ee46e585c7dd49bf30c7c13bcf2637ff2bd52078c558b4b6a4598c0b3ffbebfe87588c391f9a002cac4f636efa392df04275266fee08156` |
| Canonical Manifest | `v5-manifest.yaml` | `651a274b11c54e391ef375e7bd2caf2f68e53c2d79efff417ac83722c914d546a30efe3d671772c51317da7c982483be763002291a4a2490eeebf0afdb46b385` |
| AEIP Frame Schema | `schemas/aeip/aeip-frame-schema.json` | `2696805e40a11c02fbcbda706f0fa70a9ac0e61354ec4a289ca1cda3e6a31b090fda5763baef62bf6cd1809e0a222f9adc78a91c93731091d26593bc5cf1868b` |
| Civic Charter Schema | `schemas/aeip/civic-charter-schema.json` | `e6f054e269813ccb112a0e3aef54f4dd39507d1016efa39bf336ef75adbd792fd1eb27a2e86615ac688d16128a2df10e8382bacf224ffdc2ea29bb1d31349188` |
| Custodial Controls Matrix | `schemas/aeip/ccm-schema.json` | `4e6c51e2d955d5c244111bf043464781e7095e2417d2fb29f64dab869b06a0445b0eeec93eebec8d011eb0f9316a6d6086883e5d6da7bc862757681eca1bc31a` |
| Governance Decision Summary | `schemas/aeip/gds-schema.json` | `882906300e84c8c94783c730f247dbab11cd9c235a69496bd9dcf318400104dffed6e4de8a6cd621936745c90d33499d1192cdf95f3735c22f8c899f58474cf2` |
| Incident Report Schema | `schemas/aeip/incident-report-schema.json` | `a22c219055aa7d9ebbece1b03ee7da1f0ca761717fb7b4a6aed5983a9378473bf6115634a955cd61d17ab95f2a4eecbc8954667c1c789835b891533bc3439a64` |
| Instruction Log Schema | `schemas/aeip/instruction-log-schema.json` | `f8e51f3a56cf2220d8b60c79ddc65fc7d6852ff49677b660113ced9be113089da36bb91b85d6e4fbd765554fbdc3ec080fd8f1fd7e4bba4bfe04163ce4ac6a2d` |
| Modelcard Schema | `schemas/aeip/modelcard-schema.json` | `22d99946b624a08fb39ed95344ccadc12f9c6a4496c576c21893f1952bad8743c996244f7f6935240246390fc59482e256034682be44348be1d57e76f2a849e5` |
| Temporal Exchange Chain Log | `schemas/aeip/tecl-schema.json` | `eeb68604c28f9f341ae2a4f74ca0e249d8899e0cdb35ee1af1a16107da6a1ff4fb27855b8bad9645e26152714abcc9d7b57d4ba23345f3a580f7035c5b4e6413` |

Recompute the hashes locally using `sha512sum <path>` and match each value against this table. If any checksum diverges, halt verification and notify the maintainers immediately.

## Signature Verification Procedure
1. Ensure the canonical manifest (`v5-manifest.yaml`) is present alongside this notice.
2. Install repository dependencies (`pip install -e .` or equivalent virtual environment setup).
3. Execute `python tools/verify-aeip-signatures.py --manifest v5-manifest.yaml`.
4. Confirm the script reports valid signatures for all AEIP payloads and that the manifest hash chain is intact.

## Governance Statement
This is the canonical public record of the AI OSI Stack v5. Any derivative without this notice is non-canonical. Store the notice with the manifest, PDF, and AEIP schemas to preserve verifiability across mirrors and archives.

“Chapters 19A–24 incorporated into canonical v5.0 build on 2025-11-07.  
No change to version or cryptographic lineage; additional chapters extend interpretive scope only.”

### Newly Added Canonical Texts (SHA-512)
| Chapter | Path | SHA-512 |
| --- | --- | --- |
| 19A – Usage, Trust & Social Reality | `source/interpretive/chapter-19a-usage-and-trust.tex` | `d9c4e99655fb913da1aad63cfe31ceaaa5e0051afb9bfd73477a9fec2166e30573efc5e94be90997534147635639e3a4523d82d932d58eb2a5578262f71be385` |
| 20 – Rhetoric & Semantics | `source/interpretive/chapter-20-rhetoric-and-semantics.tex` | `50843a24110495c7016ae228becb1298c23538cdf65a3a68f221b8401e31d80b52cda9cb1ac18f6d53ff42ce6d42624830d043a2d8ce7bac043398fafe7fbc97` |
| 21 – The Companion Trap | `source/interpretive/chapter-21-companion-trap.tex` | `501825c46b0c968b14ee3f6cc4817d23f7d46965160e6ea7989e0471042e9c2f7232c758ae7c7ee2a975b2fd2e5f3205b832a28fc7c747d87056f601c5390d53` |
| 22 – Persona Architecture | `source/interpretive/chapter-22-persona-architecture.tex` | `d2cbdb666ce5eb71e292e5194c2e773f370f1e2aa982faed4cfdce7833bd95ef9b714d94c273dd2150e04f2e4c14214939366a6c8a6e8daa8b62fbc8775c9d3a` |
| 23 – Therapy-Tech & Governance of Care | `source/interpretive/chapter-23-therapy-tech-and-governance-of-care.tex` | `844ffd66fac8d1cb5dae77b0e63cab5d9b4de56ecbb092c22fe655c5e71c7fc2564ba1037cfe73ca44d270a9d4abd48e64b67736128316285531e53ab16b506d` |
| 24 – Governance Paradox | `source/interpretive/chapter-24-governance-paradox.tex` | `5d3150cf7b71880b1af6763b72cc4df22d4c477670c336bd8bed933755bedb3105d609ec347875fa1f0cadb533ab6a0027cb30909a02fcce3e91e199b8722e56` |

### Editorial Coherence Update — 2025-11-07
No version change; editorial coherence adjustments only.

| File | Path | SHA-512 |
| --- | --- | --- |
| Schema Reference Index | `schemas/readme.md` | `7bd47969d7e6cceb28e86b793e1bb0ccd01d6fc6dab950005cc062cb34b1017777ac10543bfefaa110e1d126bee5caaad07aec729fccef5e97fcace91d283313` |
| Inventory Map | `audits/00-inventory-map.md` | `dc05337895736809e2fc277f2aa104caf35af0aebcc459913bb90c3b4f8b95cc6ac23ec9b35bc0f16e221fded4a40ea103553033df7297d4f134f2c87853c977` |
| Naming Changes Patch | `audits/10-naming-changes.patch` | `d7c8301b5688201bc1f8a250087895aef21a8f93ed920d065c650a732a5e9871accb00a68ec8b8f22677eb4785e4fc55fa5b2194da83b56cd6e203cb8b328680` |
| Naming Coherence Report | `audits/10-naming-coherence.md` | `d8122a0bff33e677a8917cddd6271304121613e72932ff6773af0ce77471dcfdc23c77555e2c61efef8d1aa4553ccd3579d25df1e0de5f00bce1827b1f38db58` |
| Traceability Matrix | `audits/20-traceability.csv` | `be9b690a658bfc9c52b3af0de5632703500886551326ccdb2337fe5e6687065f4ea310d8896a8d1a74d39f935f92a4eb4abd550c30019341a47ff2816c62718d` |
| Missing Links Log | `audits/21-missing-links.md` | `3f5d931a0aacaa2fb4d9be3c782fb9098d1ff8456ecc106838a0f80458a1d6de79eff875019537fb9ac8fc75c57266a85953383c77caabf6203296274e2caa05` |
| Orphan Schemas Report | `audits/22-orphan-schemas.md` | `ad999471fa6ddaac766af017b1ae5a075340aee483b33325ebe3b24b5cddf665cc6bd4b6f21fa85b7f1b8f83aa2b249b963e1a014fccb5cda8cf82e203cac4c4` |
| Triple Register Audit | `audits/30-triple-register-audit.md` | `fd0d4711851651cc4dcbc47add07f2cdabdc2e3ba0ffe96457b18686892206392eb2e3f6fb0fb45d46bdb48cb876c1e89845b7481bd7592590bce3f1d50681e2` |
| Triple Register Patch Log | `audits/30-triple-register-changes.patch` | `dcf38febbb16fc30637d4ffdc1d1c50101c658552095732a71880b2d41d1124eb4a6a43f41abf486bd51c04122814388f5c6d1a3fefea1fa9aa332297602726d` |
| Glossary Patch Log | `audits/40-glossary-changes.patch` | `13b424d5cc2abb607a070e5152d9faea766b6be7cb70ded4d6f1963e94addb796fda4ae603ae4e7ab48f122167fa7594a08134472f8532e3d18b18dac2da55b5` |
| Glossary Gap Report | `audits/40-missing-glossary-terms.md` | `c4a3b3b3ba79a85b49ab0d4ca8543c772bb270d9eeb8f6fc39f6b60729aac517464eb7df9042686f71e8a8fa8f9f5d76f2e58180a02f31b04ffafc54cda75cbc` |
| Policy Continuity Report | `audits/50-policy-continuity.md` | `ffa7be569c74a60fcbdcb27708aa11cfefefb9e9708df669f25151c156e7e48fa9cb853230ea748a4f5c5029e336928dbc7f0ae828fe190ebbca62f9d5320b0f` |
| Integrity Recap | `audits/60-integrity-recap.md` | `6a882d17dda1ff4b43a89d9b47b98f8dc1f0fd95fa3f24ad46349ea181827dbc379877319b4f1b9c4371bdf4159f2c1b847ef0835cd454a925057c7435cd61c0` |
| Conceptual Coherence Summary | `audits/99-conceptual-coherence-summary.md` | `3daf7d4b110b14a9c3136980d0798242db7de02a69e7f0a297551b7a087c3deebc364153fc845492ba82764aef5eb15cbf2a16b728b29164fb57db454849c64f` |
| Build Guidance | `audits/BUILD_LOCAL.md` | `aa37a7bd1ca4fa1234d31a49ada559cfa906ca6e95024045cc23709aeca33456543f9b2aee4da1c214b68594f27030bf0d136ee37d2854a811e1a91947347bae` |
| Standards Alignment Brief | `docs/standards-alignment-brief.md` | `1d1a8f9d8da0d3d84436d1205ae08a5a2ca785e211d69035e11cd5183ff487eb8ed8f4927984bda3a21708d702d0ae8a05ac22402f4862fec2bb6dee105d01bb` |
