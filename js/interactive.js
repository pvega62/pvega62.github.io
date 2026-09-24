// Scroll Progress Bar
(function () {
  var progressContainer = document.createElement('div');
  progressContainer.className = 'progress-container';
  var progressBar = document.createElement('div');
  progressBar.className = 'progress-bar';
  progressBar.id = 'myBar';
  progressContainer.appendChild(progressBar);
  
  if (document.body && !document.getElementById('myBar')) {
    document.body.insertBefore(progressContainer, document.body.firstChild);
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      if (!document.getElementById('myBar')) {
        document.body.insertBefore(progressContainer, document.body.firstChild);
      }
    });
  }

  window.addEventListener('scroll', function () {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = height ? (winScroll / height) * 100 : 0;
    var bar = document.getElementById('myBar');
    if (bar) bar.style.width = scrolled + '%';
  });
})();

// 3D Parallax Card Tilt (desktop / pointer devices only)
(function () {
  if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (window.location.href.indexOf('uxwriting') !== -1) return;
  document.querySelectorAll('.sample-card').forEach(function (card) {
    card.addEventListener('mousemove', function (e) {
      var rect = card.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      var centerX = rect.width / 2;
      var centerY = rect.height / 2;
      var rotateX = ((y - centerY) / centerY) * -5;
      var rotateY = ((x - centerX) / centerX) * 5;
      card.style.transform = 'perspective(1000px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) scale3d(1.02, 1.02, 1.02)';
    });
    card.addEventListener('mouseleave', function () {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
      card.style.transition = 'transform 0.5s ease-out';
    });
    card.addEventListener('mouseenter', function () {
      card.style.transition = 'none';
    });
  });
})();

// Constellation & Celestial Engine (Vibrant, Elegant, and Non-Distracting for Portfolio)
(function () {
  var sections = document.querySelectorAll('.hero-section, .bg-custom-dark:not(.navbar)');
  sections.forEach(function (section) {
    if (!section.querySelector('.particles-canvas')) {
      var canvas = document.createElement('canvas');
      canvas.className = 'particles-canvas';
      canvas.setAttribute('aria-hidden', 'true');
      section.insertBefore(canvas, section.firstChild);
    }
  });

  var canvases = document.querySelectorAll('.particles-canvas');
  canvases.forEach(function(canvas) {
    if (!canvas || !canvas.getContext) return;
    var ctx = canvas.getContext('2d');
    var isMobile = window.innerWidth < 768;
    var count = isMobile ? 45 : 85;
    var particles = [];
    var shootingStars = [];
    var nextShootingStarTime = Date.now() + 5000;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = canvas.parentElement.offsetWidth;
      var h = canvas.parentElement.offsetHeight;
      canvas.width = Math.floor(w * dpr);
      canvas.height = Math.floor(h * dpr);
      canvas.style.width = w + 'px';
      canvas.style.height = h + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    resize();
    window.addEventListener('resize', resize, { passive: true });

    // Ambient Star
    function Particle() {
      this.reset(true);
    }
    Particle.prototype.reset = function (initial) {
      var w = canvas.parentElement.offsetWidth || window.innerWidth;
      var h = canvas.parentElement.offsetHeight || 500;
      this.x = Math.random() * w;
      this.y = Math.random() * h;
      var angle = Math.random() * Math.PI * 2;
      var speed = Math.random() * 0.12 + 0.04;
      this.vx = Math.cos(angle) * speed;
      this.vy = Math.sin(angle) * speed;
      this.r = Math.random() * 1.2 + 0.7; // 0.7px to 1.9px
      this.isBright = Math.random() < 0.15;
      if (this.isBright) this.r = Math.random() * 1.0 + 1.8;
      this.baseAlpha = Math.random() * 0.35 + 0.35; // 0.35 to 0.70 clear visibility
      this.twinklePhase = Math.random() * Math.PI * 2;
      this.twinkleSpeed = Math.random() * 0.03 + 0.015;
      // Starlight hues: diamond white, soft celestial amber, cool topaz
      var tints = ['240, 238, 233', '248, 218, 148', '198, 232, 255'];
      this.tint = tints[Math.floor(Math.random() * tints.length)];
    };
    Particle.prototype.update = function (w, h) {
      this.x += this.vx;
      this.y += this.vy;
      this.twinklePhase += this.twinkleSpeed;
      if (this.x < -10) this.x = w + 10;
      if (this.x > w + 10) this.x = -10;
      if (this.y < -10) this.y = h + 10;
      if (this.y > h + 10) this.y = -10;
    };
    Particle.prototype.draw = function () {
      var alpha = Math.max(0.15, Math.min(0.85, this.baseAlpha + 0.20 * Math.sin(this.twinklePhase)));
      var w = canvas.parentElement.offsetWidth || window.innerWidth;
      var h = canvas.parentElement.offsetHeight || 500;
      var tdx = this.x - w * 0.50;
      var tdy = (this.y - h * 0.48) * 2.0;
      var textDist = Math.sqrt(tdx * tdx + tdy * tdy);
      var isUnderText = textDist < (isMobile ? 190 : 290);
      var drawRadius = this.r;
      if (isUnderText) {
        alpha *= 0.18; // Soften ambient stars under headline & typewriter text
        drawRadius *= 0.75; // Shrunk star diameter so text is completely crisp
      }
      ctx.beginPath();
      ctx.arc(this.x, this.y, drawRadius, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(' + this.tint + ',' + alpha.toFixed(2) + ')';
      ctx.fill();
    };

    for (var p = 0; p < count; p++) particles.push(new Particle());

    // Constellation helper
    function createConstellation(config) {
      return {
        id: config.id,
        color: config.color,
        haloColor: config.haloColor || config.color,
        fillPolygons: config.fillPolygons || [],
        isFeatured: !!config.isFeatured,
        x: config.x,
        y: config.y,
        vx: config.vx || 0.05,
        vy: config.vy || -0.03,
        angle: config.angle || 0,
        vAngle: config.vAngle || 0.0004,
        scale: config.scale || 1,
        nodes: config.nodes,
        edges: config.edges,
        flareAngle: 0,
        update: function(w, h) {
          this.x += this.vx;
          this.y += this.vy;
          this.angle += this.vAngle;
          this.flareAngle += 0.005;

          // Gentle orbital deflection around central headline text
          var tdx = this.x - w * 0.50;
          var tdy = (this.y - h * 0.48) * 2.0;
          var textDist = Math.sqrt(tdx * tdx + tdy * tdy);
          var shieldRadius = isMobile ? 220 : 340;
          if (textDist < shieldRadius && textDist > 0) {
            var force = (1 - textDist / shieldRadius) * 0.75;
            this.x += (tdx / textDist) * force;
            this.y += (tdy / textDist) * (force * 0.45);
          }

          var margin = 110;
          if (this.x < -margin) this.x = w + margin;
          if (this.x > w + margin) this.x = -margin;
          if (this.y < -margin) this.y = h + margin;
          if (this.y > h + margin) this.y = -margin;
        },
        draw: function() {
          var cos = Math.cos(this.angle);
          var sin = Math.sin(this.angle);
          var pts = [];
          for (var i = 0; i < this.nodes.length; i++) {
            var n = this.nodes[i];
            var scaledDx = n.dx * this.scale;
            var scaledDy = n.dy * this.scale;
            var nx = this.x + (scaledDx * cos - scaledDy * sin);
            var ny = this.y + (scaledDx * sin + scaledDy * cos);
            pts.push({
              x: nx,
              y: ny,
              r: n.r * (isMobile ? 0.85 : 1.05),
              isAlpha: n.isAlpha,
              isVega: n.isVega,
              name: n.name
            });
          }

          // Text zone damping: if constellation center OR any star node is within central text area, soften intensity
          var pw = canvas.parentElement.offsetWidth || window.innerWidth;
          var ph = canvas.parentElement.offsetHeight || 500;
          var textCenterX = pw * 0.50;
          var textCenterY = ph * 0.48;
          var tdx = this.x - textCenterX;
          var tdy = (this.y - textCenterY) * 2.0;
          var textDist = Math.sqrt(tdx * tdx + tdy * tdy);
          var shieldLimit = isMobile ? 220 : 340;
          var isNearText = textDist < shieldLimit;

          if (!isNearText) {
            for (var k = 0; k < pts.length; k++) {
              var ndx = pts[k].x - textCenterX;
              var ndy = (pts[k].y - textCenterY) * 2.0;
              if (Math.sqrt(ndx * ndx + ndy * ndy) < (isMobile ? 190 : 290)) {
                isNearText = true;
                break;
              }
            }
          }

          var textDamping = isNearText ? 0.15 : 1.0;

          // 0. Soft translucent geometric nebula fill (for Lyra harp body) - suppressed near text
          if (this.fillPolygons && this.fillPolygons.length > 0 && !isNearText) {
            ctx.save();
            for (var f = 0; f < this.fillPolygons.length; f++) {
              var poly = this.fillPolygons[f];
              if (poly.length < 3) continue;
              ctx.beginPath();
              ctx.moveTo(pts[poly[0]].x, pts[poly[0]].y);
              for (var pi = 1; pi < poly.length; pi++) {
                ctx.lineTo(pts[poly[pi]].x, pts[poly[pi]].y);
              }
              ctx.closePath();
              ctx.fillStyle = this.haloColor.replace('ALPHA', this.isFeatured ? '0.09' : '0.05');
              ctx.fill();
            }
            ctx.restore();
          }

          // 1. Draw connecting constellation lines
          for (var e = 0; e < this.edges.length; e++) {
            var p1 = pts[this.edges[e][0]];
            var p2 = pts[this.edges[e][1]];
            if (!p1 || !p2) continue;

            // Radiant outer glow
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = this.haloColor.replace('ALPHA', ((this.isFeatured ? 0.40 : 0.28) * textDamping).toFixed(2));
            ctx.lineWidth = isMobile ? 1.8 : (this.isFeatured ? 2.8 : 2.2);
            ctx.stroke();

            // Crisp inner constellation line
            ctx.beginPath();
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = this.color.replace('ALPHA', ((this.isFeatured ? 0.85 : 0.70) * textDamping).toFixed(2));
            ctx.lineWidth = isMobile ? 1.1 : (this.isFeatured ? 1.5 : 1.3);
            ctx.stroke();
            ctx.restore();
          }

          // 2. Draw stars & beacon flares
          for (var i = 0; i < pts.length; i++) {
            var pt = pts[i];
            var starRadius = isNearText ? pt.r * 0.85 : pt.r;

            if (pt.isAlpha) {
              var isV = !!pt.isVega;
              var pulse = 1 + 0.16 * Math.sin(Date.now() * 0.0035);

              // Pulsing beacon ring for highlighted Vega (only in open skies)
              if (isV && !isNearText) {
                var ringPhase = (Date.now() % 2600) / 2600;
                var ringRadius = starRadius + ringPhase * 28;
                var ringAlpha = (1 - ringPhase) * 0.55;
                ctx.beginPath();
                ctx.arc(pt.x, pt.y, ringRadius, 0, Math.PI * 2);
                ctx.strokeStyle = this.haloColor.replace('ALPHA', ringAlpha.toFixed(2));
                ctx.lineWidth = 1.0;
                ctx.stroke();
              }

              // Multi-stage radiant corona
              var coronaRadius = starRadius * (isV ? 4.6 : 3.8) * pulse * (isNearText ? 0.5 : 1.0);
              var grad = ctx.createRadialGradient(pt.x, pt.y, 0, pt.x, pt.y, coronaRadius);
              grad.addColorStop(0, this.haloColor.replace('ALPHA', (isV ? 0.65 : 0.55) * textDamping));
              grad.addColorStop(0.4, this.haloColor.replace('ALPHA', (isV ? 0.30 : 0.20) * textDamping));
              grad.addColorStop(1, 'rgba(0,0,0,0)');
              ctx.fillStyle = grad;
              ctx.beginPath();
              ctx.arc(pt.x, pt.y, coronaRadius, 0, Math.PI * 2);
              ctx.fill();

              // 8-point diffraction spike flare for Vega (4-point for Hamal) - suppressed in text zone
              if (!isNearText) {
                ctx.save();
                ctx.translate(pt.x, pt.y);
                ctx.rotate(this.flareAngle);

                var spikeLen = starRadius * (isV ? 3.8 : 3.0);
                // Primary cross rays
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.90)';
                ctx.lineWidth = isV ? 1.2 : 1.0;
                ctx.beginPath();
                ctx.moveTo(-spikeLen, 0);
                ctx.lineTo(spikeLen, 0);
                ctx.moveTo(0, -spikeLen);
                ctx.lineTo(0, spikeLen);
                ctx.stroke();

                // Secondary 45° diagonal sub-spikes
                ctx.strokeStyle = this.haloColor.replace('ALPHA', isV ? '0.55' : '0.35');
                ctx.lineWidth = 0.8;
                var subLen = spikeLen * (isV ? 0.65 : 0.50);
                ctx.beginPath();
                ctx.moveTo(-subLen, -subLen);
                ctx.lineTo(subLen, subLen);
                ctx.moveTo(subLen, -subLen);
                ctx.lineTo(-subLen, subLen);
                ctx.stroke();
                ctx.restore();
              }
            } else {
              // Secondary star soft glow aura
              var auraGrad = ctx.createRadialGradient(pt.x, pt.y, 0, pt.x, pt.y, starRadius * 2.2);
              auraGrad.addColorStop(0, this.haloColor.replace('ALPHA', (0.40 * textDamping).toFixed(2)));
              auraGrad.addColorStop(1, 'rgba(0,0,0,0)');
              ctx.fillStyle = auraGrad;
              ctx.beginPath();
              ctx.arc(pt.x, pt.y, starRadius * 2.2, 0, Math.PI * 2);
              ctx.fill();
            }

            // Brilliant white star core
            ctx.beginPath();
            ctx.arc(pt.x, pt.y, Math.max(1.5, starRadius * 0.85), 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(255, 255, 255, ' + (isNearText ? '0.35' : '1.0') + ')';
            ctx.fill();
          }
        }
      };
    }

    var parentW = canvas.parentElement.offsetWidth || window.innerWidth;
    var parentH = canvas.parentElement.offsetHeight || 500;

    // 1. ARIES (The Ram) - Warm Starlight Gold
    var aries = createConstellation({
      id: 'aries',
      color: 'rgba(245, 206, 117, ALPHA)',
      haloColor: 'rgba(255, 222, 140, ALPHA)',
      x: isMobile ? parentW * 0.20 : parentW * 0.18,
      y: isMobile ? parentH * 0.20 : parentH * 0.25,
      vx: 0.04,
      vy: -0.02,
      angle: 0.18,
      vAngle: 0.0003,
      scale: isMobile ? 0.70 : 1.05,
      nodes: [
        { dx: -78, dy: 32, r: 2.8, name: 'Mesarthim' },
        { dx: -42, dy: 16, r: 3.4, name: 'Sheratan' },
        { dx: 4,   dy: -6, r: 4.8, name: 'Hamal', isAlpha: true },
        { dx: 52,  dy: -20, r: 3.2, name: 'Bharani' },
        { dx: 98,  dy: -12, r: 2.6, name: 'Botein' }
      ],
      edges: [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 4]
      ]
    });

    // 2. LYRA (Featuring Vega) - Highlighted Radiant Diamond Azure & Celestial Topaz
    var lyra = createConstellation({
      id: 'lyra',
      isFeatured: true,
      color: 'rgba(96, 205, 255, ALPHA)',
      haloColor: 'rgba(56, 189, 248, ALPHA)',
      fillPolygons: [
        [2, 3, 5, 4], // Quad harp body (zeta, delta, sulafat, sheliak)
        [0, 1, 2]     // Upper triangle linking Vega to the harp
      ],
      x: isMobile ? parentW * 0.80 : parentW * 0.82,
      y: isMobile ? parentH * 0.75 : parentH * 0.32,
      vx: -0.035,
      vy: 0.025,
      angle: -0.15,
      vAngle: -0.0003,
      scale: isMobile ? 0.72 : 1.10,
      nodes: [
        { dx: 0,   dy: 0,   r: 6.2, name: 'Vega', isAlpha: true, isVega: true },
        { dx: 28,  dy: -22, r: 2.7, name: 'ε Lyrae' },
        { dx: 34,  dy: 18,  r: 3.0, name: 'ζ Lyrae' },
        { dx: 68,  dy: 12,  r: 2.8, name: 'δ Lyrae' },
        { dx: 62,  dy: 56,  r: 3.6, name: 'Sheliak' },
        { dx: 98,  dy: 48,  r: 3.4, name: 'Sulafat' }
      ],
      edges: [
        [0, 1],
        [0, 2],
        [2, 3],
        [3, 5],
        [5, 4],
        [4, 2]
      ]
    });

    // Shooting Star (Calm, rare, elegant)
    function spawnShootingStar(w, h) {
      var startX = Math.random() * (w * 0.8);
      var startY = Math.random() * (h * 0.35);
      var angle = (Math.PI / 4) + (Math.random() - 0.5) * 0.25;
      var speed = Math.random() * 4 + 5;
      shootingStars.push({
        x: startX,
        y: startY,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        length: Math.random() * 50 + 60,
        opacity: 0.85,
        life: 0,
        maxLife: Math.random() * 40 + 35
      });
      nextShootingStarTime = Date.now() + (Math.random() * 15000 + 15000); // 15-30s interval
    }

    var mouseX = -9999, mouseY = -9999;
    var parentEl = canvas.parentElement;
    parentEl.addEventListener('mousemove', function (e) {
      var rect = parentEl.getBoundingClientRect();
      mouseX = e.clientX - rect.left;
      mouseY = e.clientY - rect.top;
    }, { passive: true });
    parentEl.addEventListener('mouseleave', function () {
      mouseX = -9999;
      mouseY = -9999;
    }, { passive: true });

    // Mobile touch interaction
    parentEl.addEventListener('touchstart', function (e) {
      if (e.touches && e.touches[0]) {
        var rect = parentEl.getBoundingClientRect();
        mouseX = e.touches[0].clientX - rect.left;
        mouseY = e.touches[0].clientY - rect.top;
      }
    }, { passive: true });
    parentEl.addEventListener('touchmove', function (e) {
      if (e.touches && e.touches[0]) {
        var rect = parentEl.getBoundingClientRect();
        mouseX = e.touches[0].clientX - rect.left;
        mouseY = e.touches[0].clientY - rect.top;
      }
    }, { passive: true });
    parentEl.addEventListener('touchend', function () {
      mouseX = -9999;
      mouseY = -9999;
    }, { passive: true });

    function frame() {
      var w = parentEl.offsetWidth;
      var h = parentEl.offsetHeight;
      ctx.clearRect(0, 0, w, h);

      // Check shooting star trigger
      if (Date.now() > nextShootingStarTime) {
        spawnShootingStar(w, h);
      }

      // Draw and update ambient particles
      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        var dx0 = p.x - mouseX;
        var dy0 = p.y - mouseY;
        var dist0 = Math.sqrt(dx0 * dx0 + dy0 * dy0);
        if (dist0 < 85 && dist0 > 0) {
          p.x += (dx0 / dist0) * 0.25; // Gentle, smooth deflection
          p.y += (dy0 / dist0) * 0.25;
        }
        p.update(w, h);
        p.draw();

        // Atmospheric connecting lines between nearby ambient stars
        for (var j = i + 1; j < particles.length; j++) {
          var p2 = particles[j];
          var dx = p.x - p2.x;
          var dy = p.y - p2.y;
          var d = Math.sqrt(dx * dx + dy * dy);
          if (d < 105) {
            var midX = (p.x + p2.x) * 0.5;
            var midY = (p.y + p2.y) * 0.5;
            var mtdx = midX - w * 0.50;
            var mtdy = (midY - h * 0.48) * 2.0;
            var mDist = Math.sqrt(mtdx * mtdx + mtdy * mtdy);
            var latticeAlpha = (0.18 * (1 - d / 105));
            if (mDist < (isMobile ? 190 : 290)) {
              latticeAlpha *= 0.10; // Zero distraction through headline
            }
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = 'rgba(215, 222, 232, ' + latticeAlpha.toFixed(3) + ')';
            ctx.lineWidth = 0.7;
            ctx.stroke();
          }
        }
      }

      // Draw shooting stars
      for (var s = shootingStars.length - 1; s >= 0; s--) {
        var ss = shootingStars[s];
        ss.x += ss.vx;
        ss.y += ss.vy;
        ss.life++;
        var currentAlpha = ss.opacity * (1 - ss.life / ss.maxLife);
        if (currentAlpha <= 0 || ss.life >= ss.maxLife) {
          shootingStars.splice(s, 1);
          continue;
        }

        var tailX = ss.x - (ss.vx / 5) * ss.length;
        var tailY = ss.y - (ss.vy / 5) * ss.length;
        var grad = ctx.createLinearGradient(tailX, tailY, ss.x, ss.y);
        grad.addColorStop(0, 'rgba(255, 255, 255, 0)');
        grad.addColorStop(0.7, 'rgba(255, 235, 175, ' + (currentAlpha * 0.5).toFixed(2) + ')');
        grad.addColorStop(1, 'rgba(255, 255, 255, ' + currentAlpha.toFixed(2) + ')');

        ctx.save();
        ctx.beginPath();
        ctx.moveTo(tailX, tailY);
        ctx.lineTo(ss.x, ss.y);
        ctx.strokeStyle = grad;
        ctx.lineWidth = 1.4;
        ctx.stroke();
        ctx.restore();
      }

      // Update and draw signature constellations
      aries.update(w, h);
      aries.draw();

      lyra.update(w, h);
      lyra.draw();

      requestAnimationFrame(frame);
    }
    frame();
  });
})();
// Carousel Touch Swipe Support
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var carousels = document.querySelectorAll('.carousel');
    carousels.forEach(function(carousel) {
      var touchStartX = 0;
      var touchEndX = 0;
      
      carousel.addEventListener('touchstart', function(event) {
        touchStartX = event.changedTouches[0].screenX;
      }, {passive: true});
      
      carousel.addEventListener('touchend', function(event) {
        touchEndX = event.changedTouches[0].screenX;
        handleSwipe();
      }, {passive: true});
      
      function handleSwipe() {
        var swipeThreshold = 40; // minimum distance to trigger swipe
        if (touchEndX < touchStartX - swipeThreshold) {
          // swipe left -> next
          var nextBtn = carousel.querySelector('.carousel-control-next');
          if (nextBtn) nextBtn.click();
        }
        if (touchEndX > touchStartX + swipeThreshold) {
          // swipe right -> prev
          var prevBtn = carousel.querySelector('.carousel-control-prev');
          if (prevBtn) prevBtn.click();
        }
      }
    });
  });
})();
