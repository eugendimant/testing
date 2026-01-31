<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crimson Corridor: Outbreak Run</title>
    <style>
        :root {
            color-scheme: dark;
            --bg: #0b0b10;
            --panel: #151522;
            --accent: #e94560;
            --accent-bright: #ff4d6d;
            --text: #f7f7fb;
            --muted: #b2b2c2;
            --good: #4cd964;
            --warning: #f5a623;
        }

        * {
            box-sizing: border-box;
            font-family: "Inter", "Segoe UI", sans-serif;
        }

        body {
            margin: 0;
            background: radial-gradient(circle at top, #1b1b2f, #0b0b10 60%);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        header {
            padding: 24px clamp(20px, 6vw, 60px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }

        header h1 {
            margin: 0;
            font-size: clamp(24px, 3vw, 34px);
            letter-spacing: 0.08em;
        }

        header p {
            margin: 4px 0 0;
            color: var(--muted);
            font-size: 14px;
        }

        .container {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 320px;
            gap: 24px;
            padding: 24px clamp(20px, 6vw, 60px) 40px;
            flex: 1;
        }

        .panel {
            background: var(--panel);
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }

        #game-wrap {
            position: relative;
            overflow: hidden;
            min-height: 420px;
        }

        canvas {
            width: 100%;
            height: 100%;
            display: block;
            border-radius: 12px;
            background: radial-gradient(circle at 20% 20%, #1f1f36, #0a0a12 70%);
        }

        .hud {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .hud .stat {
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            color: var(--muted);
        }

        .bar {
            position: relative;
            height: 10px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 999px;
            overflow: hidden;
        }

        .bar span {
            display: block;
            height: 100%;
            background: linear-gradient(90deg, var(--accent), var(--accent-bright));
            transition: width 0.2s ease;
        }

        .bar.health span {
            background: linear-gradient(90deg, #ff4d4d, #ff915a);
        }

        .bar.stamina span {
            background: linear-gradient(90deg, #49f2c0, #3dd5f3);
        }

        .hint {
            font-size: 13px;
            color: var(--muted);
            line-height: 1.6;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 10px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.08);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .overlay {
            position: absolute;
            inset: 0;
            background: rgba(6, 6, 12, 0.82);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 24px;
        }

        .overlay.hidden {
            display: none;
        }

        .overlay-card {
            background: rgba(15, 15, 26, 0.95);
            border-radius: 16px;
            padding: 24px;
            max-width: 520px;
            width: 100%;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        }

        .overlay-card h2 {
            margin-top: 0;
            font-size: 24px;
        }

        .button-row {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 20px;
        }

        button {
            background: var(--accent);
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 10px;
            font-size: 14px;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(233, 69, 96, 0.3);
        }

        button.secondary {
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--text);
        }

        .upgrade-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 12px;
            margin-top: 16px;
        }

        .upgrade-card {
            background: rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            padding: 14px;
            border: 1px solid transparent;
            text-align: left;
        }

        .upgrade-card h3 {
            margin: 0 0 6px;
            font-size: 14px;
        }

        .upgrade-card p {
            margin: 0;
            font-size: 12px;
            color: var(--muted);
            line-height: 1.4;
        }

        footer {
            padding: 16px clamp(20px, 6vw, 60px);
            color: var(--muted);
            font-size: 12px;
        }

        @media (max-width: 960px) {
            .container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div>
            <h1>Crimson Corridor: Outbreak Run</h1>
            <p>Survive the containment breach. Slash through infected, harvest upgrades, and keep moving.</p>
        </div>
        <div class="badge">Prototype v1.0</div>
    </header>

    <main class="container">
        <section class="panel" id="game-wrap">
            <canvas id="gameCanvas" width="960" height="540" aria-label="Crimson Corridor game canvas"></canvas>

            <div class="overlay" id="startOverlay">
                <div class="overlay-card">
                    <h2>Containment Warning</h2>
                    <p class="hint">WASD / Arrow keys to move. Space to slash. Shift to dash. P to pause. Survive the waves and pick upgrades between outbreaks.</p>
                    <div class="button-row">
                        <button id="startButton">Start Run</button>
                        <button class="secondary" id="toggleGore">Gore: On</button>
                    </div>
                </div>
            </div>

            <div class="overlay hidden" id="upgradeOverlay">
                <div class="overlay-card">
                    <h2>Field Upgrade</h2>
                    <p class="hint">Choose one enhancement before the next wave breaches containment.</p>
                    <div class="upgrade-grid" id="upgradeGrid"></div>
                </div>
            </div>

            <div class="overlay hidden" id="gameOverOverlay">
                <div class="overlay-card">
                    <h2>Outbreak Lost</h2>
                    <p class="hint" id="gameOverStats"></p>
                    <div class="button-row">
                        <button id="retryButton">Run it Back</button>
                    </div>
                </div>
            </div>
        </section>

        <aside class="panel hud">
            <div class="stat"><span>Status</span><span id="statusLabel">Idle</span></div>
            <div>
                <div class="stat"><span>Health</span><span id="healthLabel">100</span></div>
                <div class="bar health"><span id="healthBar"></span></div>
            </div>
            <div>
                <div class="stat"><span>Stamina</span><span id="staminaLabel">100</span></div>
                <div class="bar stamina"><span id="staminaBar"></span></div>
            </div>
            <div class="stat"><span>Wave</span><span id="waveLabel">0</span></div>
            <div class="stat"><span>Threats Remaining</span><span id="threatLabel">0</span></div>
            <div class="stat"><span>Score</span><span id="scoreLabel">0</span></div>
            <div class="stat"><span>Combo</span><span id="comboLabel">x1</span></div>
            <div class="stat"><span>High Score</span><span id="highScoreLabel">0</span></div>
            <div class="hint">
                <strong>Improvements active:</strong>
                <ul>
                    <li>Adaptive wave escalation with elite infected.</li>
                    <li>Upgrade armory between waves.</li>
                    <li>Gore &amp; splatter particle system.</li>
                    <li>Drop-based recovery items.</li>
                    <li>Persistent high score tracking.</li>
                </ul>
            </div>
        </aside>
    </main>

    <footer>
        Built for fast keyboard play. Tune the difficulty by surviving longer waves.
    </footer>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const startOverlay = document.getElementById("startOverlay");
        const upgradeOverlay = document.getElementById("upgradeOverlay");
        const gameOverOverlay = document.getElementById("gameOverOverlay");
        const upgradeGrid = document.getElementById("upgradeGrid");
        const statusLabel = document.getElementById("statusLabel");
        const healthLabel = document.getElementById("healthLabel");
        const staminaLabel = document.getElementById("staminaLabel");
        const waveLabel = document.getElementById("waveLabel");
        const threatLabel = document.getElementById("threatLabel");
        const scoreLabel = document.getElementById("scoreLabel");
        const comboLabel = document.getElementById("comboLabel");
        const highScoreLabel = document.getElementById("highScoreLabel");
        const healthBar = document.getElementById("healthBar");
        const staminaBar = document.getElementById("staminaBar");
        const gameOverStats = document.getElementById("gameOverStats");
        const startButton = document.getElementById("startButton");
        const retryButton = document.getElementById("retryButton");
        const toggleGoreButton = document.getElementById("toggleGore");

        const keys = new Set();
        let lastTime = 0;
        let goreEnabled = true;
        let gameState = "title";
        let wave = 0;
        let score = 0;
        let combo = 1;
        let comboTimer = 0;
        let highScore = Number(localStorage.getItem("crimsonHighScore") || 0);

        const player = {
            x: canvas.width / 2,
            y: canvas.height / 2,
            radius: 14,
            speed: 2.6,
            dashSpeed: 6,
            dashCooldown: 0,
            dashCost: 30,
            health: 100,
            maxHealth: 100,
            stamina: 100,
            maxStamina: 100,
            staminaRegen: 18,
            damage: 22,
            swingCooldown: 0,
            swingRange: 64,
        };

        const enemies = [];
        const particles = [];
        const splatters = [];
        const pickups = [];

        const upgrades = [
            {
                title: "Hardened Armor",
                description: "+25 max health and +10% damage reduction.",
                apply: () => {
                    player.maxHealth += 25;
                    player.health = Math.min(player.health + 25, player.maxHealth);
                    player.damageReduction = (player.damageReduction || 0) + 0.1;
                },
            },
            {
                title: "Adrenal Surge",
                description: "+0.35 move speed and +20 stamina.",
                apply: () => {
                    player.speed += 0.35;
                    player.maxStamina += 20;
                    player.stamina = Math.min(player.stamina + 20, player.maxStamina);
                },
            },
            {
                title: "Ripper Edge",
                description: "+8 damage and +15 slash range.",
                apply: () => {
                    player.damage += 8;
                    player.swingRange += 15;
                },
            },
            {
                title: "Pulse Injector",
                description: "+6 stamina regeneration per second.",
                apply: () => {
                    player.staminaRegen += 6;
                },
            },
            {
                title: "Dash Capacitor",
                description: "Reduce dash cooldown by 40%.",
                apply: () => {
                    player.dashCooldownReduction = (player.dashCooldownReduction || 0) + 0.4;
                },
            },
            {
                title: "Slayer Instinct",
                description: "+0.25 combo multiplier decay time.",
                apply: () => {
                    player.comboGrace = (player.comboGrace || 1.6) + 0.25;
                },
            },
        ];

        function resetGame() {
            player.x = canvas.width / 2;
            player.y = canvas.height / 2;
            player.health = player.maxHealth = 100;
            player.stamina = player.maxStamina = 100;
            player.speed = 2.6;
            player.damage = 22;
            player.swingRange = 64;
            player.swingCooldown = 0;
            player.staminaRegen = 18;
            player.dashCooldown = 0;
            player.dashCost = 30;
            player.damageReduction = 0;
            player.dashCooldownReduction = 0;
            player.comboGrace = 1.6;
            enemies.length = 0;
            particles.length = 0;
            splatters.length = 0;
            pickups.length = 0;
            wave = 0;
            score = 0;
            combo = 1;
            comboTimer = 0;
        }

        function startGame() {
            resetGame();
            gameState = "playing";
            startOverlay.classList.add("hidden");
            gameOverOverlay.classList.add("hidden");
            statusLabel.textContent = "Engaged";
            nextWave();
        }

        function nextWave() {
            wave += 1;
            const baseCount = 4 + wave * 2;
            const eliteCount = Math.floor(wave / 3);
            spawnEnemies(baseCount, "runner");
            spawnEnemies(eliteCount, "brute");
            statusLabel.textContent = `Wave ${wave}`;
        }

        function spawnEnemies(count, type) {
            for (let i = 0; i < count; i += 1) {
                const edge = Math.floor(Math.random() * 4);
                let x = 0;
                let y = 0;
                const margin = 40;
                if (edge === 0) {
                    x = Math.random() * canvas.width;
                    y = -margin;
                } else if (edge === 1) {
                    x = canvas.width + margin;
                    y = Math.random() * canvas.height;
                } else if (edge === 2) {
                    x = Math.random() * canvas.width;
                    y = canvas.height + margin;
                } else {
                    x = -margin;
                    y = Math.random() * canvas.height;
                }
                const isBrute = type === "brute";
                enemies.push({
                    x,
                    y,
                    radius: isBrute ? 20 : 14,
                    speed: isBrute ? 1.2 + wave * 0.05 : 1.8 + wave * 0.08,
                    health: isBrute ? 90 + wave * 12 : 40 + wave * 6,
                    maxHealth: isBrute ? 90 + wave * 12 : 40 + wave * 6,
                    type,
                });
            }
        }

        function spawnPickup(x, y) {
            const roll = Math.random();
            if (roll > 0.3) {
                return;
            }
            const type = roll < 0.1 ? "stamina" : "health";
            pickups.push({
                x,
                y,
                radius: 10,
                type,
                ttl: 12,
            });
        }

        function addSplatter(x, y) {
            if (!goreEnabled) {
                return;
            }
            splatters.push({
                x,
                y,
                radius: 12 + Math.random() * 18,
                alpha: 0.8,
            });
        }

        function addBloodBurst(x, y) {
            if (!goreEnabled) {
                return;
            }
            for (let i = 0; i < 14; i += 1) {
                const angle = Math.random() * Math.PI * 2;
                const speed = 1 + Math.random() * 3.5;
                particles.push({
                    x,
                    y,
                    vx: Math.cos(angle) * speed,
                    vy: Math.sin(angle) * speed,
                    life: 0.7 + Math.random() * 0.6,
                    size: 2 + Math.random() * 3,
                });
            }
        }

        function update(delta) {
            if (gameState !== "playing") {
                return;
            }

            const deltaSeconds = delta / 1000;

            if (comboTimer > 0) {
                comboTimer -= deltaSeconds;
                if (comboTimer <= 0) {
                    combo = 1;
                }
            }

            const moveX = (keys.has("ArrowRight") || keys.has("d") ? 1 : 0) - (keys.has("ArrowLeft") || keys.has("a") ? 1 : 0);
            const moveY = (keys.has("ArrowDown") || keys.has("s") ? 1 : 0) - (keys.has("ArrowUp") || keys.has("w") ? 1 : 0);
            const magnitude = Math.hypot(moveX, moveY) || 1;
            let speed = player.speed;

            if (keys.has("Shift") && player.stamina > player.dashCost && player.dashCooldown <= 0) {
                player.stamina -= player.dashCost;
                player.dashCooldown = 1.6 * (1 - (player.dashCooldownReduction || 0));
                speed = player.dashSpeed;
            }

            player.x += (moveX / magnitude) * speed;
            player.y += (moveY / magnitude) * speed;

            player.x = Math.max(player.radius, Math.min(canvas.width - player.radius, player.x));
            player.y = Math.max(player.radius, Math.min(canvas.height - player.radius, player.y));

            if (player.swingCooldown > 0) {
                player.swingCooldown -= deltaSeconds;
            }

            if (player.dashCooldown > 0) {
                player.dashCooldown -= deltaSeconds;
            }

            player.stamina = Math.min(player.maxStamina, player.stamina + player.staminaRegen * deltaSeconds);

            if (keys.has(" ") && player.swingCooldown <= 0 && player.stamina >= 12) {
                player.swingCooldown = 0.35;
                player.stamina -= 12;
                performAttack();
            }

            updateEnemies(deltaSeconds);
            updateParticles(deltaSeconds);
            updatePickups(deltaSeconds);

            if (enemies.length === 0) {
                gameState = "upgrade";
                showUpgrades();
            }
        }

        function performAttack() {
            const range = player.swingRange;
            let hit = false;
            enemies.forEach((enemy) => {
                const distance = Math.hypot(enemy.x - player.x, enemy.y - player.y);
                if (distance < range + enemy.radius) {
                    enemy.health -= player.damage;
                    hit = true;
                    addBloodBurst(enemy.x, enemy.y);
                    addSplatter(enemy.x, enemy.y);
                }
            });
            if (hit) {
                combo = Math.min(6, combo + 0.2);
                comboTimer = player.comboGrace || 1.6;
            }
        }

        function updateEnemies(deltaSeconds) {
            for (let i = enemies.length - 1; i >= 0; i -= 1) {
                const enemy = enemies[i];
                const dx = player.x - enemy.x;
                const dy = player.y - enemy.y;
                const dist = Math.hypot(dx, dy) || 1;
                enemy.x += (dx / dist) * enemy.speed;
                enemy.y += (dy / dist) * enemy.speed;

                if (dist < enemy.radius + player.radius) {
                    const damage = (enemy.type === "brute" ? 16 : 10) * deltaSeconds;
                    const reduction = player.damageReduction || 0;
                    player.health -= damage * (1 - reduction);
                }

                if (enemy.health <= 0) {
                    enemies.splice(i, 1);
                    score += Math.floor((enemy.type === "brute" ? 80 : 45) * combo);
                    spawnPickup(enemy.x, enemy.y);
                }
            }

            if (player.health <= 0) {
                endGame();
            }
        }

        function updateParticles(deltaSeconds) {
            for (let i = particles.length - 1; i >= 0; i -= 1) {
                const particle = particles[i];
                particle.life -= deltaSeconds;
                particle.x += particle.vx;
                particle.y += particle.vy;
                particle.vx *= 0.95;
                particle.vy *= 0.95;
                if (particle.life <= 0) {
                    particles.splice(i, 1);
                }
            }
            for (let i = splatters.length - 1; i >= 0; i -= 1) {
                const splatter = splatters[i];
                splatter.alpha -= deltaSeconds * 0.04;
                if (splatter.alpha <= 0) {
                    splatters.splice(i, 1);
                }
            }
        }

        function updatePickups(deltaSeconds) {
            for (let i = pickups.length - 1; i >= 0; i -= 1) {
                const pickup = pickups[i];
                pickup.ttl -= deltaSeconds;
                if (pickup.ttl <= 0) {
                    pickups.splice(i, 1);
                    continue;
                }
                const distance = Math.hypot(pickup.x - player.x, pickup.y - player.y);
                if (distance < pickup.radius + player.radius) {
                    if (pickup.type === "health") {
                        player.health = Math.min(player.maxHealth, player.health + 25);
                    } else {
                        player.stamina = Math.min(player.maxStamina, player.stamina + 30);
                    }
                    pickups.splice(i, 1);
                }
            }
        }

        function render() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            ctx.save();
            ctx.fillStyle = "rgba(255, 255, 255, 0.04)";
            for (let x = 0; x < canvas.width; x += 40) {
                ctx.fillRect(x, 0, 1, canvas.height);
            }
            for (let y = 0; y < canvas.height; y += 40) {
                ctx.fillRect(0, y, canvas.width, 1);
            }
            ctx.restore();

            splatters.forEach((splatter) => {
                ctx.beginPath();
                ctx.fillStyle = `rgba(153, 10, 30, ${splatter.alpha})`;
                ctx.arc(splatter.x, splatter.y, splatter.radius, 0, Math.PI * 2);
                ctx.fill();
            });

            pickups.forEach((pickup) => {
                ctx.beginPath();
                ctx.fillStyle = pickup.type === "health" ? "rgba(255, 120, 120, 0.9)" : "rgba(80, 200, 255, 0.9)";
                ctx.arc(pickup.x, pickup.y, pickup.radius, 0, Math.PI * 2);
                ctx.fill();
            });

            enemies.forEach((enemy) => {
                ctx.beginPath();
                ctx.fillStyle = enemy.type === "brute" ? "#8a1f2b" : "#c0293d";
                ctx.arc(enemy.x, enemy.y, enemy.radius, 0, Math.PI * 2);
                ctx.fill();
                ctx.fillStyle = "rgba(0, 0, 0, 0.4)";
                ctx.fillRect(enemy.x - enemy.radius, enemy.y - enemy.radius - 6, enemy.radius * 2, 4);
                ctx.fillStyle = "#ff4d6d";
                ctx.fillRect(enemy.x - enemy.radius, enemy.y - enemy.radius - 6, (enemy.health / enemy.maxHealth) * enemy.radius * 2, 4);
            });

            ctx.beginPath();
            ctx.fillStyle = "#f7f7fb";
            ctx.arc(player.x, player.y, player.radius, 0, Math.PI * 2);
            ctx.fill();

            if (player.swingCooldown > 0) {
                ctx.beginPath();
                ctx.strokeStyle = "rgba(255, 77, 109, 0.6)";
                ctx.lineWidth = 3;
                ctx.arc(player.x, player.y, player.swingRange, 0, Math.PI * 2);
                ctx.stroke();
            }

            particles.forEach((particle) => {
                ctx.beginPath();
                ctx.fillStyle = "rgba(198, 25, 48, 0.9)";
                ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                ctx.fill();
            });

            ctx.fillStyle = "rgba(255, 255, 255, 0.6)";
            ctx.font = "14px sans-serif";
            ctx.fillText(`Wave ${wave}`, 20, 28);
        }

        function updateHud() {
            healthLabel.textContent = Math.ceil(player.health);
            staminaLabel.textContent = Math.ceil(player.stamina);
            waveLabel.textContent = wave;
            threatLabel.textContent = enemies.length;
            scoreLabel.textContent = score;
            comboLabel.textContent = `x${combo.toFixed(1)}`;
            highScoreLabel.textContent = highScore;
            healthBar.style.width = `${(player.health / player.maxHealth) * 100}%`;
            staminaBar.style.width = `${(player.stamina / player.maxStamina) * 100}%`;
        }

        function showUpgrades() {
            upgradeGrid.innerHTML = "";
            const choices = [...upgrades].sort(() => 0.5 - Math.random()).slice(0, 3);
            choices.forEach((upgrade) => {
                const card = document.createElement("div");
                card.className = "upgrade-card";
                card.innerHTML = `<h3>${upgrade.title}</h3><p>${upgrade.description}</p>`;
                const button = document.createElement("button");
                button.textContent = "Install";
                button.addEventListener("click", () => {
                    upgrade.apply();
                    upgradeOverlay.classList.add("hidden");
                    gameState = "playing";
                    nextWave();
                });
                card.appendChild(button);
                upgradeGrid.appendChild(card);
            });
            upgradeOverlay.classList.remove("hidden");
        }

        function endGame() {
            gameState = "gameover";
            statusLabel.textContent = "Down";
            gameOverStats.textContent = `You held for ${wave} waves with a score of ${score}.`;
            if (score > highScore) {
                highScore = score;
                localStorage.setItem("crimsonHighScore", highScore);
                gameOverStats.textContent += " New personal best.";
            }
            gameOverOverlay.classList.remove("hidden");
        }

        function loop(timestamp) {
            const delta = timestamp - lastTime;
            lastTime = timestamp;
            if (gameState === "playing") {
                update(delta);
            }
            if (gameState === "paused") {
                statusLabel.textContent = "Paused";
            }
            render();
            updateHud();
            requestAnimationFrame(loop);
        }

        function togglePause() {
            if (gameState === "playing") {
                gameState = "paused";
            } else if (gameState === "paused") {
                gameState = "playing";
                statusLabel.textContent = "Engaged";
            }
        }

        window.addEventListener("keydown", (event) => {
            if (event.key === "p" || event.key === "P") {
                togglePause();
                return;
            }
            keys.add(event.key);
        });

        window.addEventListener("keyup", (event) => {
            keys.delete(event.key);
        });

        startButton.addEventListener("click", startGame);
        retryButton.addEventListener("click", startGame);
        toggleGoreButton.addEventListener("click", () => {
            goreEnabled = !goreEnabled;
            toggleGoreButton.textContent = `Gore: ${goreEnabled ? "On" : "Off"}`;
        });

        requestAnimationFrame(loop);
    </script>
</body>
</html>
