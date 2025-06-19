#!/usr/bin/env python3
"""
Script to complete the main pre-production services landing page
"""

def get_main_content():
    """Return the main content sections for the pre-production landing page"""
    return '''
        <!-- Introduction Section -->
        <section class="py-16">
            <div class="container mx-auto px-4">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-4xl font-bold text-vietnam-orange mb-6">
                        Comprehensive Pre-Production Services
                    </h2>
                    <p class="text-xl text-gray-300 max-w-4xl mx-auto mb-8">
                        From initial concept to production-ready planning, our expert team provides comprehensive pre-production services that set the foundation for successful films, TV shows, commercials, and digital content worldwide.
                    </p>
                </div>
                
                <div class="grid md:grid-cols-3 gap-8 mb-16">
                    <div class="text-center">
                        <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center text-2xl font-bold mx-auto mb-4">🎬</div>
                        <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Creative Excellence</h3>
                        <p class="text-gray-300">Expert scriptwriting, storyboarding, and creative development services that bring your vision to life with professional precision.</p>
                    </div>
                    <div class="text-center">
                        <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center text-2xl font-bold mx-auto mb-4">📋</div>
                        <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Strategic Planning</h3>
                        <p class="text-gray-300">Comprehensive budgeting, scheduling, and logistics coordination that ensures your production runs smoothly from day one.</p>
                    </div>
                    <div class="text-center">
                        <div class="bg-vietnam-orange text-black rounded-full w-16 h-16 flex items-center justify-center text-2xl font-bold mx-auto mb-4">🌍</div>
                        <h3 class="text-xl font-semibold text-vietnam-orange mb-3">Global Reach</h3>
                        <p class="text-gray-300">Worldwide network of professionals providing local expertise and international quality standards for productions anywhere.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Services Grid Section -->
        <section class="py-16 bg-vietnam-dark">
            <div class="container mx-auto px-4">
                <div class="max-w-6xl mx-auto">
                    <h2 class="text-3xl font-bold text-vietnam-orange mb-12 text-center">Our Pre-Production Services</h2>
                    
                    <!-- Creative & Development -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Creative & Development</h3>
                        <div class="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
                            <a href="/pre-production-services/scriptwriting/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Scriptwriting</h4>
                                <p class="text-gray-300 text-sm">Professional screenwriting services</p>
                            </a>
                            <a href="/pre-production-services/script-consultation/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Script Consultation</h4>
                                <p class="text-gray-300 text-sm">Expert script polishing and refinement</p>
                            </a>
                            <a href="/pre-production-services/storyboarding/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Storyboarding</h4>
                                <p class="text-gray-300 text-sm">Visual storytelling and planning</p>
                            </a>
                            <a href="/pre-production-services/concept-development/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Concept Development</h4>
                                <p class="text-gray-300 text-sm">Creative ideation and planning</p>
                            </a>
                            <a href="/pre-production-services/creative-direction/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Creative Direction</h4>
                                <p class="text-gray-300 text-sm">Artistic vision and leadership</p>
                            </a>
                            <a href="/pre-production-services/moodboard-creation/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Moodboards</h4>
                                <p class="text-gray-300 text-sm">Visual style guides and lookbooks</p>
                            </a>
                            <a href="/pre-production-services/pitch-deck-design/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Pitch Decks</h4>
                                <p class="text-gray-300 text-sm">Compelling presentations and treatments</p>
                            </a>
                        </div>
                    </div>

                    <!-- Casting & Talent -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Casting & Talent</h3>
                        <div class="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
                            <a href="/pre-production-services/casting-services/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Casting Services</h4>
                                <p class="text-gray-300 text-sm">Actors, models, and extras</p>
                            </a>
                            <a href="/pre-production-services/voiceover-casting/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Voiceover Casting</h4>
                                <p class="text-gray-300 text-sm">Professional voice talent</p>
                            </a>
                            <a href="/pre-production-services/talent-coordination/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Talent Coordination</h4>
                                <p class="text-gray-300 text-sm">Artist management and scheduling</p>
                            </a>
                            <a href="/pre-production-services/union-talent-management/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Union Management</h4>
                                <p class="text-gray-300 text-sm">Union and non-union talent handling</p>
                            </a>
                        </div>
                    </div>

                    <!-- Location & Permits -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Location & Permits</h3>
                        <div class="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
                            <a href="/pre-production-services/location-scouting-services/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Location Scouting</h4>
                                <p class="text-gray-300 text-sm">Perfect filming locations worldwide</p>
                            </a>
                            <a href="/pre-production-services/location-management/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Location Management</h4>
                                <p class="text-gray-300 text-sm">On-site coordination and management</p>
                            </a>
                            <a href="/pre-production-services/film-permit-acquisition/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Permit Acquisition</h4>
                                <p class="text-gray-300 text-sm">Filming permits and licenses</p>
                            </a>
                            <a href="/pre-production-services/site-surveys/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Site Surveys</h4>
                                <p class="text-gray-300 text-sm">Technical location assessment</p>
                            </a>
                            <a href="/pre-production-services/production-insurance/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Production Insurance</h4>
                                <p class="text-gray-300 text-sm">Comprehensive coverage solutions</p>
                            </a>
                        </div>
                    </div>

                    <!-- Budgeting & Scheduling -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Budgeting & Scheduling</h3>
                        <div class="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
                            <a href="/pre-production-services/production-budgeting/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Production Budgeting</h4>
                                <p class="text-gray-300 text-sm">Financial planning and management</p>
                            </a>
                            <a href="/pre-production-services/cost-estimation/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Cost Estimation</h4>
                                <p class="text-gray-300 text-sm">Accurate budget analysis</p>
                            </a>
                            <a href="/pre-production-services/production-scheduling/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Production Scheduling</h4>
                                <p class="text-gray-300 text-sm">Timeline management and coordination</p>
                            </a>
                            <a href="/pre-production-services/call-sheets/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Call Sheets</h4>
                                <p class="text-gray-300 text-sm">Shooting schedules and coordination</p>
                            </a>
                        </div>
                    </div>

                    <!-- Crew & Logistics -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Crew & Logistics</h3>
                        <div class="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
                            <a href="/pre-production-services/line-producing-services/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Line Producing</h4>
                                <p class="text-gray-300 text-sm">Production management expertise</p>
                            </a>
                            <a href="/pre-production-services/crew-hiring/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Crew Hiring</h4>
                                <p class="text-gray-300 text-sm">Professional crew recruitment</p>
                            </a>
                            <a href="/pre-production-services/fixer-services-local/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Local Fixers</h4>
                                <p class="text-gray-300 text-sm">Local production support</p>
                            </a>
                            <a href="/pre-production-services/travel-logistics/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Travel Logistics</h4>
                                <p class="text-gray-300 text-sm">Travel and accommodation coordination</p>
                            </a>
                            <a href="/pre-production-services/equipment-planning/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Equipment Planning</h4>
                                <p class="text-gray-300 text-sm">Production gear coordination</p>
                            </a>
                            <a href="/pre-production-services/catering-services/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Catering Services</h4>
                                <p class="text-gray-300 text-sm">On-set catering coordination</p>
                            </a>
                        </div>
                    </div>

                    <!-- Legal & Administrative -->
                    <div class="mb-12">
                        <h3 class="text-2xl font-bold text-vietnam-orange mb-6">Legal & Administrative</h3>
                        <div class="grid md:grid-cols-3 lg:grid-cols-4 gap-4">
                            <a href="/pre-production-services/contract-management/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Contract Management</h4>
                                <p class="text-gray-300 text-sm">Legal documentation handling</p>
                            </a>
                            <a href="/pre-production-services/talent-releases/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Talent Releases</h4>
                                <p class="text-gray-300 text-sm">Legal agreements and releases</p>
                            </a>
                            <a href="/pre-production-services/location-agreements/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Location Agreements</h4>
                                <p class="text-gray-300 text-sm">Location contracts and agreements</p>
                            </a>
                            <a href="/pre-production-services/licensing-rights/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">Licensing & Rights</h4>
                                <p class="text-gray-300 text-sm">Intellectual property management</p>
                            </a>
                            <a href="/pre-production-services/covid-compliance/" class="service-card bg-vietnam-darker border border-gray-700 rounded-lg p-4 hover:border-vietnam-orange transition-all duration-300">
                                <h4 class="text-vietnam-orange font-semibold mb-2">COVID Compliance</h4>
                                <p class="text-gray-300 text-sm">Safety protocols and compliance</p>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

def main():
    """Complete the main pre-production services landing page"""
    print("🚀 Completing main pre-production services landing page...")
    
    try:
        with open('pre-production-services/index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add main content after hero section
        main_content = get_main_content()
        content = content.replace('        </section>', f'        </section>{main_content}', 1)
        
        # Write completed content
        with open('pre-production-services/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Main pre-production services landing page completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error completing main page: {e}")
        return False

if __name__ == "__main__":
    main()
